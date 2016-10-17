while(True):
    user_input = input("Please enter a value: ")
    if "quit" in user_input:
        break
    elif "dnp" in user_input:
        continue
    else:
        print(user_input)
