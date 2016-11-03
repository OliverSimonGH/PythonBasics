academy_dict = {
    'Location': "Newport",
    'Course': "Software Engineering",
    'Length': 3,
    'Languages': "Python, HTML, CSS, Javascript"
}

# for i, o in  enumerate(academy_dict):
#     if len(academy_dict[o]) > 5:
#         print("Index: {} \nIndex Value: {} \nValue: {}\n".format(i, o, academy_dict[o]))

def int_val(dict):
    for key in dict:
        if type(dict[key]) is int:
            return key
        return "There is no value of int."

def return_key(dict):
    for key, value in enumerate(dict):
        if type(key) is int:
            return key;

int_val(academy_dict)
return_key(academy_dict)
