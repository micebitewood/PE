import java.util.*;
import java.math.*;

public class Test {
	static int sum(String s)
	{
		int result=0;
		for(int i=0;i<s.length();i++)
			result+=s.charAt(i)-'0';
		return result;
	}
	public static void main(String[] args)
	{
		BigInteger n, m;
		int max=0;
		int x;
		for(int i=1;i<100;i++)
		{
			n=new BigInteger(""+i);
			m=n;
			x=sum(n.toString());
			if(max<x)
				max=x;
			for(int j=1;j<i;j++)
			{
				n=n.multiply(m);
				x=sum(n.toString());
				if(max<x)
					max=x;
			}
		}
		System.out.println(max);
	}
}
