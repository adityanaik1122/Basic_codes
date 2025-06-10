def Addition(A,B):
    Result = 0
    Result = A + B
    return Result

def main():
    print("Enter first Number : ") 
    No1 = int(input())

    print("Enter second Number : ")
    No2 = int(input())

    ret = Addition(No1, No2)

    print("Addition is :",ret)

if __name__=="__main__":
    main()    


