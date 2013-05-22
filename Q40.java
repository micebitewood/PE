public class Q40
{
    public static void main(String args[])
    {
        String s=".";

        for(int i=1;i<100000;i++)
            s+=i;
        int[] a=new int[7];
        int j=1;
        int product=1;
        for(int i=0;i<7;i++)
        {
            a[i]=s.charAt(j)-'0';
            j*=10;
            product*=a[i];
        }
        System.out.print(product);
    }
}
