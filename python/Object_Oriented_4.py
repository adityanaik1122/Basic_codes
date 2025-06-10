class Employee:
    CompanyName = "Marvellous"      #class Variable

    def __init__(self,A,B,C):
        self.Name = A                # Instance variable
        self.Salary = B              # Instance variable
        self.City = C                # Instance variable

    def __del__(self):
        print("Inside destructor")      #Desctructor

    def DisplayInfo(self):           # Instance Method    
        print("Inside display method info")
        
        print("employee name : "+self.Name)
        print("employee salary : ",self.Salary)
        print("employee city : "+self.City)

    def DisplayCompanyDetails(cls):    #class method
        printf("Compani main"+cls.CompanyName)

def main():
    print("Class Variable"+Employe.CompanyName)

    emp1 = Employee('Rahul',15000,'Pune')
    emp2 = Employee('Aditya',25000,'mumbai')
    emp3 = Employee('Rohit',14000,'nashik')

    print("employee name : "+emp1.Name)
    print("employee salary : ",emp1.Salary)
    print("employee city : "+emp1.City)

    
if __name__=="__main__":
    main()    

