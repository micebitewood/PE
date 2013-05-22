import java.io.*;

public class Q4
{
    public static boolean is_palindromic(int i)
    {
        int j=i;
        int t=0;
        int s=0;

        while(j!=0)
        {
            t=j%10;
            s*=10;
            s+=t;
            j=j/10;
        }
        if(s==i)
            return true;
        return false;
    }
    public static void main(String[] args)
    {
        FileWriter fw=new FileWriter("test");
        BufferedWriter bw=new BufferedWriter(fw);
        int n;
        for(int j=1;j<=90;j++)
        {
            for(int k=1;k<=j;k++)
            {
                n=(100-j)*(100-k);
                if(is_palindromic(n))
                    break;
            }
        }
        bw.write(n);
        bw.flush();
        bw.close();
        fw.close();
    }
}
