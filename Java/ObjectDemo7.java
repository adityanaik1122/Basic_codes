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

    public String toString()
    {
        return this.name+" "+this.rollno+" "+this.marks;
    }
}

class ObjectDemo7
{
    public static void main(String A[])
    {
        student sobj = new student("Sagar",11,87);
       
        System.out.print(sobj.toString());
    }
}