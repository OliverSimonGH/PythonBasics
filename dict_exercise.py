student_dict = {
    '01':"Oliver",
    '02':"Morgan",
    '03':"Dom",
    '04':"Laura",
    '05':"Destiny",
    '06':"Megan",
    '07':"Jen",
    '08':"Jack",
    '09':"Thomas",
    '10':"Sarah",
}

# Getting third item in dictionary
print(student_dict.get("03"))

#Getting rid of the 2nd student in dictionary and storing it in variable.
student = student_dict.pop("02")
print(student)

#Adding the 2nd student back into the dictionary via the variable
student_dict["02"] = student
print(student_dict.get("02"))

#Pop returns the values of an item within a dictionary
#Popitem returns the key and value of an item in the dictionary as a "mini list"

#If the key does not exist, then print the error message
print(student_dict.pop("11", "Sorry, that student number does not exist."))

#Find the value "Jen" in the dictionary and printing out the index.
for key, value in enumerate(student_dict):
    if student_dict[value] == "Jen":
        print(value)

#If the key exists in the dictionary, return True.
print("07" in student_dict.keys())

#If the value exists in the dictionary, return True.
print("Jen" in student_dict.values())
