# 153 = ( 1*1*1) + (5*5*5) + (3*3*3) = 153

num = int(input(" enter the number : "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    cube =  digit ** 3
    sum = sum + cube
    temp = temp // 10


if sum == num:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number")