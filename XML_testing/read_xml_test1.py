#read_xml_test1.py
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag)
print('Root Elements:', len(root))
for child in root:
    print(child.tag, child.attrib)
    print(child.tag, 'Elements:',len(child))
    print(child[0].tag, child[0].text) #Rank
    print(child[1].tag, child[1].text) #Year
    print(child[2].tag, child[2].text) #GDPPC

print('*' * 30)

for child in root:
    print(child.tag, child.attrib)
    print(child.tag, 'Elements:',len(child))

    for element in child:
        print('\t', element.tag, end=' ')

        if len(element.attrib) > 0 :
            print(element.attrib, end=' ')

        if element.text is not None:
            print('=', element.text)
        else:
            print()

print('*' * 30)

print(tree.findall("."))
print(tree)
print(root.findall("."))
print(root.tag)
print(  root.findall(".//year/..[@name='Singapore']")[0].tag, end='')
print(  root.findall(".//year/..[@name='Singapore']")[0].attrib )
print(  root.findall(".//year/..[@name='Singapore']")[0].text )
