
def main():
    Ans = 0

    try:
        print("Enter first number :")
        no1 = int(input())

        print("Enter Second number :")
        no2 = int(input())
    
        Ans = no1/no2
    except ZeroDivisionError as zobj:
        print("Exception occour due to second input :",zobj)
        
    except ValueError as vobj:
        print("Exception occour due to second input :",vobj)   
         
    print("Division is :",Ans)

if __name__ == "__main__":
    main()    