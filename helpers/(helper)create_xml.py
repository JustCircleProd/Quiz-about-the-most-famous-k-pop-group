import xml.etree.ElementTree as ET
import os

base_path = os.path.join(os.getcwd(), 'simple_images')
root = ET.Element('data')
id = 1
for name in os.listdir(base_path):
    answer = ET.Element('answer')
    answer.text = name
    images_path = os.path.join(base_path, name)
    for image_name in os.listdir(images_path):
        id_json = ET.Element('id')
        id_json.text = str(id)
        answer.append(id_json)
        id += 1

        image = ET.Element('image')
        image.text = open(os.path.join(images_path, image_name), 'r').read()
        answer.append(image)

        break
    root.append(answer)

open('data.xml', 'wb').write(ET.tostring(root, encoding='unicode'))
        