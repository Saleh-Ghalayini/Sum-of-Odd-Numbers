x = int(input("Please enter a number: "))

sum = 0

#checking if the number if odd and if it is we add it to the variable sum then we display var sum
for i in range(x):
    if i % 2 != 0:
        sum += i
print(sum)