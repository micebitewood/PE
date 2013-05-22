public class Q30
{
    public static void main(String args[])
    {
        int[] n=new int[10];
        int i, j, s;

        for(i=0;i<10;i++)
        {
            n[i]=i;
            for(j=0;j<4;j++)
                n[i]*=i;
        }
        s=0;
        for(i=2;i<354294;i++)
        {
            j=i;
            int sum=0;
            while(j!=0)
            {
                sum+=n[j%10];
                j=j/10;
            }
            if(sum==i)
                s+=i;
        }
        System.out.print(s);
    }
}
