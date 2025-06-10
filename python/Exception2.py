
def main():
    
    print("Enter first number :")
    no1 = int(input())

    print("Enter Second number :")
    no2 = int(input())

    Ans = 0
    try:
        Ans = no1/no2
    except ZeroDivisionError:
        print("Exception occour due to second input")
        
    print("Division is :",Ans)

if __name__ == "__main__":
    main()    