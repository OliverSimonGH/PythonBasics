int_list = [10, 5]

#Checks first two Values of list and swaps thema ccordingly
def check_value(input_list, start):
    if(start == len(input_list) - 1):
        return
    elif(input_list[start] > input_list[start+1]):
        current = input_list[start]
        input_list[start] = input_list[start + 1]
        input_list[start + 1] = current
    return input_list

print(check_value(int_list, 0, 4))
