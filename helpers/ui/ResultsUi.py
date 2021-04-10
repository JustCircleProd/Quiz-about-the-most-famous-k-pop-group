# -*- coding: utf-8 -*

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 400)
        Form.setMinimumSize(QtCore.QSize(540, 400))
        Form.setMaximumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"resources\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: #2c2a2b;")
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(35, 130, 470, 260))
        self.image.setStyleSheet("border: 2 solid #535152;")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(r"resources\congrat_picture.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.amount_of_questions = QtWidgets.QLabel(Form)
        self.amount_of_questions.setEnabled(True)
        self.amount_of_questions.setGeometry(QtCore.QRect(40, 10, 471, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amount_of_questions.sizePolicy().hasHeightForWidth())
        self.amount_of_questions.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ponter")
        font.setPixelSize(40)
        self.amount_of_questions.setFont(font)
        self.amount_of_questions.setStyleSheet("color: rgb(11, 191, 47);")
        self.amount_of_questions.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_of_questions.setObjectName("amount_of_questions")
        self.comment = QtWidgets.QLabel(Form)
        self.comment.setEnabled(True)
        self.comment.setGeometry(QtCore.QRect(40, 60, 470, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comment.sizePolicy().hasHeightForWidth())
        self.comment.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ponter")
        font.setPixelSize(22)
        self.comment.setFont(font)
        self.comment.setStyleSheet("color: #f0f0f0;")
        self.comment.setLineWidth(2)
        self.comment.setTextFormat(QtCore.Qt.AutoText)
        self.comment.setAlignment(QtCore.Qt.AlignCenter)
        self.comment.setWordWrap(True)
        self.comment.setObjectName("comment")
        self.roses = QtWidgets.QLabel(Form)
        self.roses.setGeometry(QtCore.QRect(0, 0, 540, 400))
        self.roses.setStyleSheet("background-color: none;")
        self.roses.setText("")
        self.roses.setScaledContents(True)
        self.roses.setObjectName("roses")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OnlyBtsFuns"))
        self.amount_of_questions.setText(_translate("Form", "10 правильных ответов из 10"))
        self.comment.setText(_translate("Form", "Пришли сюда, чтобы сфоткаться и поздравить тебя Как видишь мы уже сфоткались"))
