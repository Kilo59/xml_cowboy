# read_xml_test1.py
import xml.etree.ElementTree as ET
import os

print('Working Directory:', os.getcwd())
tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    print(child.tag, 'Elements:', len(child))

    for element in child:
        print('\t', element.tag, end=' ')

        if len(element.attrib) > 0:
            print(element.attrib, end=' ')

        if element.text is not None:
            print('=', element.text)
        else:
            print()


print('*' * 30)

# We can remove elements using Element.remove().
# Remove all countries with a rank higher than 50:
# Add elements to remaining countries
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
    else:
        product1 = ET.SubElement(country, 'major_product1')
        product2 = ET.Element('Product2')
        product2.text = 'Stuff2'
        country.append(product2)
        product1.text = 'Stuff1'

tree.write('output.xml')
