list = ["werewolf", "jacob", "animal", "human", 20, 14]

for i in list:
    print(i)

if "werewolf" in list:
    print("The " + list[0] + " is an " + list[2] + " that is " + str(list[4]) + " years old.")

if "jacob" in list:
    print(list[1] + " is a " + list[3] + " that is " + str(list[-1]) + " years old.")
