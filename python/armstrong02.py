lower = int(input("Enter the lower limit : "))
higher = int(input("Enter the higher limit : "))


for num in range (lower, higher + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp = temp // 10 
    if num == sum:
        print( num)