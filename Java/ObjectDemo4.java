class student
{
    public String name;
    public int rollno;
    public int marks;

    public student(String str, int A, int B)
    {
        System.out.println("Inside Constructor");
        this.name = str;
        this.rollno = A;
        this.marks = B;
    }

    // 
    public Boolean equals(student obj)
    {
        if ((this.marks == obj.marks) && ((this.name).equals(obj.name)))
            {
                return true;
            }
            else
            {
                return false;
            }
        
    }

}

class ObjectDemo4
{
    public static void main(String A[])
    {
        student sobj1 = new student("Sagar",11,87);
        student sobj2 = new student("Aditya",11,87);

        if (sobj1.equals(sobj2) == true )
        {
            System.out.print("objects are equal");
        }
        else
        {
          System.out.print("objects are not equal");   
        }
       
      
        System.gc();
    }
}