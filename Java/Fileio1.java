import java.io.*;


class Fileio1
{
    public static void main(String[]args) throws Exception
    {
        File fobj = new File("Marvellous.txt");

        if(fobj.createNewFile())
        {
            System.out.println("File is created successfully");
            FileWriter fwobj = new FileWriter("Marvellous.txt");
            void ret = fwobj.write("pre-placement activity batch 53");
            System.out.println(ret);
        }
        else
        {
            System.out.println("Unable to create filea");
        }

    }
}