list = []
for i in range(0, 5):
    user_input = input("Please enter an integer please: ")
    if user_input.isdigit():
        list.append(int(user_input))
    else:
        print("I said enter a positive number")
        break
    if len(list) == 5:
        print(sum(list)/len(list))
