class Employee:
    CompanyName = "Marvellous"

    def __init__(self,A,B,C):
        print("Inside constructor")
        self.Name = A
        self.Salary = B
        self.City = C

    def __del__(self)
        print("Inside destructor")
def main():
    print("Class Variable :"+Employee.CompanyName)

    emp1 = Employee('Rahul',15000,'Pune')
    emp2 = Employee('Aditya',25000,'mumbai')
    emp3 = Employee('Rohit',14000,'nashik')

    print("employee name : "+emp1.Name)
    print("employee salary : ",emp1.Salary)
    print("employee city : "+emp1.City)

    
if __name__=="__main__":
    main()    

