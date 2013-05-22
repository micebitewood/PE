import java.util.*;
import java.math.*;

public class Test {
	public static void main(String[] args)
	{
		BigInteger[] a=new BigInteger[101];
		BigInteger[] b=new BigInteger[101];
		a[0]=new BigInteger("1");
		System.out.println(a[0]);
		a[1]=new BigInteger("1");
		int count=0;
		BigInteger com=new BigInteger("1000000");
		for(int i=2;i<=100;i++)
		{
			for(int j=1;j<i;j++)
				b[j]=a[j-1].add(a[j]);
			b[0]=new BigInteger("1");
			b[i]=new BigInteger("1");
			for(int j=0;j<=i;j++)
			{
				if(b[j].compareTo(com)>0)
					count++;
				a[j]=new BigInteger(b[j].toString());
			}
		}
		System.out.println(count);
	}
}
