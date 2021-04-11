import xml.etree.ElementTree as ET

class Db:
    def __init__(self):
        self._root = ET.parse('resources\\data.xml').getroot()
        self._count = len(self._root)

    @property
    def count(self):
        return self._count

    def get_question(self, id):
        return self._root.find(f"./question/[id='{id}']")
        