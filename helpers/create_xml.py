import xml.etree.ElementTree as ET
import os

try:
    base_path = os.path.join('resources', 'images')
    root = ET.Element('data')
    id = 1
    for name in os.listdir(base_path):
        answer = ET.Element('answer')
        answer.text = name
        images_path = os.path.join(base_path, name)
        for image_name in os.listdir(images_path):
            question = ET.Element('question')
            id_json = ET.Element('id')
            id_json.text = str(id)
            image = ET.Element('image_path')
            image.text = os.path.join(images_path, image_name)
            question.append(id_json)
            question.append(answer)
            question.append(image)
            id += 1
            root.append(question)

    open('resources\\data.xml', 'wb').write(ET.tostring(root))
except Exception as e:
    print(e)
else:
    print("Success")