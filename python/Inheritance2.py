class Circle:
    PI = 3.14

    def __init__(self, A):
        print("Inside Circle constructor") 
        self.radius = A

    def CalculateArea(self):
        Ans = 0.0
        Ans = Circle.PI * self.radius * self.radius
        return Ans    

class CircleX(Circle): 
    def __init__(self,A):
        print("Inside CircleX constructor")   
        super().__init__ (A)   
    def CalculateCircumference(self):
        Ans = 0.0
        Ans = 2 * Circle.PI * self.radius    
        return Ans

def main():
    obj = CircleX(10.5)
    ret = obj.CalculateArea()
    print("Area of circlr is ",ret)
    ret = obj.CalculateCircumference()
    print("Circumference is ",ret)



if __name__ == "__main__":
    main()    