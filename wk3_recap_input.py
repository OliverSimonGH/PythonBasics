info =[]

while(True):
    user_input = input("Please enter some values: ")
    if user_input == "save":
        break
    else:
        info.append(user_input)
        info += (user_input)

print(len(info))
print(total/len(info))
