public class Q24
{
    public static void main(String args[])
    {
        int i, j;
        boolean[] f=new boolean[10];
        int[] n=new int[10];
        long total=1000000;
        long temp;
        int count;
        long count_max=1, count_min;
        for(i=0;i<10;i++)
        {
            f[i]=true;
            count_max*=(i+1);
        }
        for(i=10;i>0;i--)
        {
            count_min=count_max/i;
            temp=count_max;
            count=i;
            do
            {
                temp=temp-count_min+1;
                count--;
            }while(temp>total && count>=0);
            System.out.println(temp+" "+total+" "+(i-count)+" "+(10-i));
            for(j=9;j>=0;j--)
            {
                if(f[j])
                    count++;
                if(count==i)
                {
                    n[10-i]=j;
                    f[j]=false;
                }
            }
            count_max/=i;
            total-=temp;
        }
        for(i=0;i<10;i++)
            System.out.print(n[i]);
    }
}
