import xml.etree.ElementTree as ET
tree = ET.parse("bill.xml")
bill = tree.getroot()

summ = 0
for b in bill[1:]:
    for i in b:
        d = i.attrib
        summ += int(d["count"]) * float(d["price"])

print(f"{summ:.2f}")
