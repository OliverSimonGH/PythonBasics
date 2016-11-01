academy_dict = {
    'Location': "Newport",
    'Course': "Software Engineering",
    'Length': 3,
    'Languages': "Python, HTML, CSS, Javascript"
}

for i, o in  enumerate(academy_dict):
    if len(academy_dict[o]) > 5:
        print("Index: {} \nIndex Value: {} \nValue: {}\n".format(i, o, academy_dict[o]))
