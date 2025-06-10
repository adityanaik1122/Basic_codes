class Arithematic:
    def __init__(self, A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Result = 0
        Result = self.No1 + self.No2
        return Result


def main():
    print("Enter first Number : ") 
    Value1 = int(input())

    print("Enter second Number : ")
    Value2 = int(input())

    obj = Arithematic(Value1, Value2)
    ret = obj.Addition()

    print("Addition is :",ret)

if __name__=="__main__":
    main()    

