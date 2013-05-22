import java.util.*;

public class Test {

	public static void main(String args[])
    {
		int[] a=new int[6968];
		int count=0;
		boolean[] f=new boolean[28124];
		int sum;
        for(int i=12;i<28124;i++)
        {
        	sum=1;
        	int k=(int)Math.sqrt(i)+1;
        	for(int j=2;j<k;j++)
        	{
        		if(i%j==0)
        		{
        			sum+=j;
        			if(j*j!=i)
        				sum+=i/j;
        		}
        	}
        	if(sum>i)
        	{
        		a[count++]=i;
        	}
        }
        for(int i=1;i<28124;i++)
        	f[i]=true;
        for(int i=0;i<count;i++)
        {
        	for(int j=i;j<count;j++)
        	{
        		if(a[i]+a[j]<28124)
        			f[a[i]+a[j]]=false;
        		else
        			break;
        	}
        }
        sum=0;
        for(int i=20162;i<28124;i++)
        {
        	if(f[i])
        		System.out.println(i);
        }
        for(int i=1;i<28124;i++)
        {
        	if(f[i])
        		sum+=i;
        }
        System.out.println(sum);
    }
}
