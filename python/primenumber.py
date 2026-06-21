# prime number 
# primer number is divisble by 1 and by itself and remender should be zero

# num = int(input("Enter the number : "))

# if (num % num == 0) and (num % 1 == 0):
#     print("it is prime number ")
# else: 
#     print("it is not a prime number ")


# print prime number in the range

lower = int(input("Enter the lower number : "))
upper = int(input("Enter the higher number : "))

for num in range ( lower, upper + 1):
    if num > 1:
        for i in range (2,num - 1):
            if num % i == 0:
                break
        else:
            print(num)