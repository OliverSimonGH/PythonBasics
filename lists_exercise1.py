#Variables
list = [31, 45, 12, 300, 40000, 2]
mean = sum(list)/ len(list)
total = 0

#Method 1 of Calculating the mean
print(mean)

#Method 2 of calculating the mean
for i in list:
    total += i
    print(total)
