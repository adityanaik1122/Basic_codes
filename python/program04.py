# prime number 
# primer number is divisble by 1 and by itself and remender should be zero

num = int(input("Enter the number : "))

if (num % num == 0) and (num % 1 == 0):
    print("it is prime number ")
else: 
    print("it is not a prime number ")