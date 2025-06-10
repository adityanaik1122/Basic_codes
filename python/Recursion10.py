# Input : 4
# Output : 10

def Add(no):
    sum = 0
    while(no >= 1):
        sum = sum + no
        no = no -1
    Add()    
    return sum    
    

def main():

    ret = Add(4)
    print(ret)
    
if __name__ == "__main__":
    main()    