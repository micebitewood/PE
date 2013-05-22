import java.util.*;

public class Test {
	static boolean[] f=new boolean[1000000];
	public static int check(int i)
	{
		int level=1;
		int j=i;
		int count=0;
		while(j>9)
		{
			j/=10;
			level*=10;;
		}
		j=i;
		for(int k=0;k<level;k++)
		{
			if(f[j])
			{
				f[j]=false;
				count++;
			}
			else if(!f[j] && !is_prime(j))
				return 0;
			j=(j%level)*10+j/level;
		}
		return count;
	}
	public static boolean is_prime(int i)
	{
		int k=(int)Math.sqrt(i);
		for(int j=2;j<k+1;j++)
			if(i%j==0)
				return false;
		return true;
	}
	public static void main(String args[])
    {
		for(int i=2;i<1000000;i++)
			f[i]=true;
		for(int i=2;i<1000000;i++)
		{
			if(f[i])
			{
				if(!is_prime(i))
					f[i]=false;
				int j=i+i;
				while(j<1000000)
				{
					f[j]=false;
					j+=i;
				}
			}
		}
		int count=0;
		for(int i=2;i<1000000;i++)
			if(f[i])
				count+=check(i);
		System.out.println(count);
    }
}
