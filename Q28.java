public class Q28
{
    public static void main(String args[])
    {
        long[][] n=new long[1001][1001];
        int i, j, k;

        for(i=0;i<1001;i++)
            for(j=0;j<1001;j++)
                n[i][j]=0;
        long total=1001*1001;
        for(k=1000;k>500;k--)
        {
            for(j=k;j>1000-k;j--)
            {
                n[1000-k][j]=total;
                total--;
            }
            for(i=1000-k;i<k;i++)
            {
                n[i][1000-k]=total;
                total--;
            }
            for(j=1000-k;j<k;j++)
            {
                n[k][j]=total;
                total--;
            }
            for(i=k;i>1000-k;i--)
            {
                n[i][k]=total;
                total--;
            }
        }
        n[500][500]=total;
        long sum=0;
        for(i=0;i<1001;i++)
        {
            sum+=n[i][i];
            sum+=n[i][1000-i];
        }
        sum-=1;
        System.out.print(sum);
    }
}
