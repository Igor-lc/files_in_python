import xml.etree.ElementTree as ET
tree = ET.parse("kinopoisk.xml")
films = tree.getroot()

print(films.tag)

for film in films:
    print(film.tag, film.attrib["name"])

    for data in film:
        if data.tag in ["year", "rating"]:
            print("    {}".format(data.text))

    for actor in film.iter("actor"):
        print("    Актер: {}".format(actor.attrib["name"]))
