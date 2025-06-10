#Method overloading - not allowed
class Base:
    def Display(self):
        print("Inside Base Display")

class Derived(Base):
    def Display(self):
        print("Inside Derived Display")


def main():
    bobj = Base()
    dobj = Derived()

    dobj.Display()
    bobj.Display()
   

if __name__ =="__main__":
    main()