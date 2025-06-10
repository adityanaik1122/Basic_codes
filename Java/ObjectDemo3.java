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
        System.out.println("this.name :"+this.name);
        System.out.println("obj.name :"+obj.name);
        return true;
    }

}

class ObjectDemo3
{
    public static void main(String A[])
    {
        student sobj1 = new student("Sagar",11,87);
        student sobj2 = new student("Aditya",11,87);

        System.out.println(sobj1.equals(sobj2));
       
      
        System.gc();
    }
}