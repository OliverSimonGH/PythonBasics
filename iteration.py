list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(list)): #Gets the index values of the entire list
    print(i) #Printing the index values

my_list = ["Swansea", "LLanelli", "New York", "Cardiff"]

for i in range(len(my_list)):
    print(i)

for key, value in enumerate(my_list):
    print(key, value)
    if "C" in value:
        print("C found at index: {0}".format(key))
