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

    protected void finalize()
    {
        System.out.println("Inside finalize method");
    }

}

class ObjectDemo1
{
    public static void main(String A[])
    {
        student sobj = new student("Sagar",11,87);

        sobj = null;
        System.gc();
    }
}