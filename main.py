import sys
import os
import random
import win32gui
from PyQt5 import QtWidgets, QtGui, QtCore

from DataModel import Db
from ui.MainUi import Ui_MainWindow
from ui.ResultsUi import Ui_Form
from ui.WarningUi import Ui_Warning


class My_window(QtWidgets.QMainWindow):
    def __init__(self, answer, image_path):
        super(My_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.answer = answer
        self.image_path = image_path
        self.number_of_question = 1
        self.amount_of_positive_answers = 0
        self.ui.image.setPixmap(self.resize_pixmap())

        self.buttons_names = {
            'Jeon Jung Kook': self.ui.jeon_jung_kook,
            'Jung Ho Seok': self.ui.junk_ho_seok,
            'Kim Nam Joon': self.ui.kim_nam_joon, 
            'Kim Seok Jin': self.ui.kim_seok_jin,
            'Kim Tae Hyung': self.ui.kim_tae_hyung, 
            'Min Yoon Gi': self.ui.min_yoon_gi,
            'Park Ji Min': self.ui.park_ji_min
        }
        for button_name in self.buttons_names.values():
            button_name.clicked.connect(self.btn_pressed)
        
        self.complements_for_positive_answer = (
            'Ты настоящий фанат!', 'За орду или за BTS?..', 'Вау!', 'Думаю, в жизни ты гений!', 'Это как раз то, что нужно!', 
            'Я тобой горжусь. Наверное', r'"55 фраз для похвалы ребёнка"', 'Ты просто радость!',
            'Экстра – класс!', 'Ты одаренный!', 'Как в сказке!', 'Даже Леон не так крут, как ты!', 'А мог бы играть в Бравл Старс...',
            'Хороший товар сам себя хвалит', 'Чрезмерная похвала - насмешка'
        )
        self.complements_for_negative_answer = (
            'Я в тебя верю!', 'В следующий раз получится!', 'Леоном не сразу становятся', 'Возьмите себя в руки!',
            'Жизнь продолжается', 'Прости...', 'Мне знакомо подобное чувство', 'Все фанаты BTS с тобой',
            'Это тяжело и несправедливо', r'"6 фраз для поддержки"', 'Неудачи - трамплин к успеху', 'И Эль Примо промахивается...'
        )
        self.ui.compliment.hide()
        self.ui.next_question.clicked.connect(self.go_to_next_question)
        self.ui.next_question.hide()
        self.ui.results.clicked.connect(self.show_result_form)
        self.ui.results.hide()
        self.result_form = Result_form()

    def resize_pixmap(self):
        pixmap = QtGui.QPixmap(os.path.normpath(self.image_path)).scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        if pixmap.height() == pixmap.width():
            self.ui.image.setGeometry(QtCore.QRect((370 - pixmap.width()) // 2, 350 - pixmap.height() + 72, pixmap.width(), pixmap.height()))
        elif pixmap.height() < 350:
            self.ui.image.setGeometry(QtCore.QRect((370 - pixmap.width()) // 2, 350 - pixmap.height(), pixmap.width(), pixmap.height()))
        else:
            self.ui.image.setGeometry(QtCore.QRect((370 - pixmap.width()) // 2, 72, pixmap.height(), pixmap.height()))
        self.ui.image.resize(pixmap.width(), pixmap.height())
        return pixmap

    def btn_pressed(self):
        for button_name in self.buttons_names.values():
                button_name.setEnabled(False)
                if self.sender() != button_name:
                    button_name.setStyleSheet("color:rgb(170, 166, 168);background-color: rgb(120, 117, 119);")
        if self.sender().text() == self.answer:
            self.amount_of_positive_answers += 1
            self.sender().setStyleSheet("color: #d7d6d6;background-color: rgb(9, 149, 37);")
            self.ui.compliment.setText(random.choice(self.complements_for_positive_answer))
        else:
            self.sender().setStyleSheet("color: #d7d6d6;background-color: rgb(208, 0, 0);")
            self.buttons_names[self.answer].setStyleSheet("color: #d7d6d6;background-color: rgb(9, 149, 37);")
            self.ui.compliment.setText(random.choice(self.complements_for_negative_answer))
        self.ui.compliment.show()
        if self.number_of_question < 10:
            self.ui.next_question.show()
        else:
            self.ui.results.show()

    def go_to_next_question(self):
        self.number_of_question += 1
        self.ui.questionNumber.setText('Вопрос {} из 10'.format(self.number_of_question))
        if self.number_of_question > 1:
            self.ui.questionNumber.setGeometry(QtCore.QRect(129, 40, 112, 24))
        self.answer, self.image_path = refresh_and_get_data()
        self.ui.image.setPixmap(self.resize_pixmap())
        for button_name in self.buttons_names.values():
            button_name.setStyleSheet("QPushButton {background-color: rgb(83, 81, 82);color: #d7d6d6;}")
            button_name.setEnabled(True)
        self.ui.compliment.hide()
        self.ui.next_question.hide()

    def show_result_form(self):
        global application
        application.hide()
        global db
        del db
        if self.amount_of_positive_answers == 1:
            amount_of_questions_text = '1 правильный ответ из 10'
        elif 2 <= self.amount_of_positive_answers < 5:
            amount_of_questions_text = '{} правильных ответа из 10'.format(self.amount_of_positive_answers)
        else:
            amount_of_questions_text = '{} правильных ответов из 10'.format(self.amount_of_positive_answers)
        self.result_form.ui.amount_of_questions.setText(amount_of_questions_text)
        if self.amount_of_positive_answers < 6:
            self.result_form.ui.comment.setText("Пришли сюда, чтобы сфоткаться и побить тебя\nКак видишь мы уже сфоткались")
            self.result_form.ui.amount_of_questions.setStyleSheet("color: rgb(255, 82, 51);")
        movie = QtGui.QMovie(r'resources\roses.gif')
        self.result_form.ui.roses.setMovie(movie)
        movie.start()
        self.result_form.show()

class Result_form(QtWidgets.QWidget):
    def __init__(self):
        super(Result_form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


class Warning_form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Warning_form, self).__init__()
        self.ui = Ui_Warning()
        self.ui.setupUi(self)

if __name__=='__main__':
    def is_PonterFont_exists():
        def callback(font, tm, font_type, names):
            names.append(font.lfFaceName)
            return True
        
        font_names = []
        hdc = win32gui.GetDC(None)
        win32gui.EnumFontFamilies(hdc, None, callback, font_names)
        win32gui.ReleaseDC(hdc, None)
        for font_name in font_names:
            if font_name == 'Ponter':
                return True
        return False

    def refresh_and_get_data():
        global questions_ids
        global db
        questions_data = db.get_question(next(questions_ids))
        return (questions_data[1].text, questions_data[2].text)

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    os.environ["QT_SCALE_FACTOR"] = "0"

    if is_PonterFont_exists():
        db = Db()
        questions_ids = random.sample(range(1, db.count + 1), 10)
        questions_ids = iter(questions_ids)
        questions_data = db.get_question(next(questions_ids))
        
        app = QtWidgets.QApplication([])
        application = My_window(questions_data[1].text, questions_data[2].text)
        application.show()
        
        sys.exit(app.exec())
    else:
        app = QtWidgets.QApplication([])
        application = Warning_form()
        application.show()
        
        sys.exit(app.exec())