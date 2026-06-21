# what is natura number
# all the positive integer numbers are natural numbers 

num = int(input("enter a number : "))

if num < 0:
    print("Please enter positive number")
else:
    sum = 0
    while num > 0:
        sum = sum + num
        num = num - 1

    print(sum)