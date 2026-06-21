#find a facotial of a number

# num = int(input(" enter the number : "))

# fact = 1

# if num < 0:
#     print("factorial of 0 does not exist")
# if num == 0:
#     print("factorial of 0 is ", 1)

# for i in range (1, num +1):
#     fact = fact * i
# print("Factorial of given number is " ,fact)


# using recursion 

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)* fact(a-1))
                
num = int(input(" enter the number : "))

result = fact(num)
print("Factorial of number is : ",result)