class student implements Cloneable
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
    public Object clone() throws CloneNotSupportedException
    {
        return super.clone();
    }


}

class ObjectDemo2
{
    public static void main(String A[]) throws Exception
    {
        student sobj = new student("Sagar",11,87);

        student sobjX = (student)sobj.clone();
    
        System.out.println(sobj.name+" "+sobj.rollno+" "+sobj.marks);
        System.out.println(sobjX.name+" "+sobjX.rollno+" "+sobjX.marks);

        System.out.println(sobj.hashCode());
        System.out.println(sobjX.hashCode());

        System.out.println(sobj.getClass());
        System.out.println(sobjX.getClass());

        sobj = null;
        System.gc();
    }
}