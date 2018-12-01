import xml.etree.ElementTree as ET

tree = ET.parse('mycountries.xml')
root = tree.getroot()

print(root[0][1].text)

print(root[0][4].text)

print(root[0][4].get('name'))

#print(root[0].find('neighbor').get('direction'))


neighbors = root[0].findall('neighbor')
for neighbor in neighbors:
    if neighbor.get('name') == 'Austria':
        print(neighbor.get('direction'))
