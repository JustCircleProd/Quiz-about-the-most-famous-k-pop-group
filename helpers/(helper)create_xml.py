import xml.etree.ElementTree as ET
import os

root = ET.Element('data')

base_path = os.path.join(os.getcwd(), 'simple_images')
for name in os.listdir(base_path):
    for image_name in os.listdir(os.path.join(base_path, name)):
        pass