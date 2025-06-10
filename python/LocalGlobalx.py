no = 11

def fun():
    global no
    print("inside fun")
    x = 21
    print("Value of x is :",x)
    no = no +1
    print("value of no",no)
   
    
def main():
    print("value of no before fun ",no)
    fun()       
    print("value of no after fun",no)

if __name__ == "__main__":
    main()    