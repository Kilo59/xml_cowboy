#read_xml_test1.py
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag)
for child in root:
    print(child.tag, child.attrib)
