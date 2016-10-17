list = ["chair", "door", "window", "window"] #Creating a list with 3 elements
print(list[0]) #Printing the first element
list[0] = "house" #Changing the first Element to "house"
print(list) #Printing all elements within list
print(len(list)) #Printing list Length
print(list[-2]) #Printing the second last element of the list
empty_list = [] #Creating new list
#print(empty_list[1]) #Returns an error because list in out of range
#empty_list[0] = 1 #Cannot input an element this way
empty_list.append(23) #Adding values to empty_list using append()
empty_list.append(5645)
empty_list.append(73)
empty_list.append(965)
print(empty_list) #Printing list

#Counting the number of elements in a listS
great_movies = list
great_movies.pop("window") #Remove "window" from the lsit
great_movies.count("chair") #Counting number of elements named "chair"
print(result)
