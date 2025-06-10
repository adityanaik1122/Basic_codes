import java.io.*;


class Fileio1
{
    public static void main(String[]args) throws Exception
    {
    
            FileWriter fwobj = new FileWriter("Marvellous.txt");
            fwobj.write("pre-placement activity batch 53");
            fwobj.newLine();
            fwobj.write("Logic building activity batch ");
            fwobj.newLine();
            fwobj.write("Python batch ");
            fwobj.newLine();
            fwobj.close();     
    
        
         
            System.out.println("File is created successfully");
            System.out.println("File is written successfully");
            
            
            FileReader frobj = new FileReader("Marvellous.txt");
            BufferedReader bobj = new BufferedReader(frobj);
            String str = null;
            while((str = bobj.readLine()) != null)
            {
                System.out.println(str);
            }
            bobj.close();
            frobj.close();
            System.out.println("File is read successfully");
            File fobj = new File("Marvellous.txt");

     
    }
}