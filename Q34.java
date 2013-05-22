import java.util.*;

public class Test {
	public static void main(String args[])
    {
        int[] n=new int[10];
        n[0]=1;
        int total=0;
        for(int i=1;i<10;i++)
        	n[i]=1;
        for(int i=2;i<10;i++)
        	n[i]=i*n[i-1];
        for(int i=10;i<2600000;i++)
        {
        	int j=i;
        	int sum=0;
        	while(j>0)
        	{
        		sum+=n[j%10];
        		j/=10;
        	}
        	if(sum==i)
        		total+=sum;
        }
        System.out.println(total);
    }
}
