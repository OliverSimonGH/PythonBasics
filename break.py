bad_words = ["fudge", "poo", "smelly", "stinky"]
my_string = input()
my_string_list = my_string.split(" ")
for word in my_string_list:
    if word in bad_words:
        print("Please do not use vulgar language")
        break #Stops for loop when it finds a vulgar word
    else:
        print (word)
