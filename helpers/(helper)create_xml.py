import xml.etree.ElementTree as ET
import os

try:
    base_path = os.path.join(os.getcwd(), 'simple_images')
    root = ET.Element('data')
    id = 1
    for name in os.listdir(base_path):
        answer = ET.Element('answer', name=name)
        images_path = os.path.join(base_path, name)
        for image_name in os.listdir(images_path):
            id_json = ET.Element('id')
            id_json.text = str(id)
            answer.append(id_json)
            image = ET.Element('image')
            image.text = (open(os.path.join(images_path, image_name), 'rb').read())
            answer.append(image)
            id += 1
        root.append(answer)

    open('resources\\data.xml', 'w').write(ET.tostring(root, encoding='unicode'))
except Exception as e:
    print(e)
else:
    print("Success")