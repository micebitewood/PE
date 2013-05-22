import java.util.*;

public class Test {
	static int level;
	static int count;
	static void fill(int[] n, int[] f, int[] result, int level)
	{
		boolean flag=true;
		if(n.length==1)
		{
			result[count]*=10;
			result[count]+=n[0];
			count++;
			flag=false;
			return;
		}
		for(int i=0;i<n.length;i++)
		{
			result[count]*=10;
			if(n.length>2)
				flag=true;
			result[count]+=n[i];
			if(flag)
				for(int j=1;j<f[n.length-1];j++)
				{
					result[count+j]=result[count];
				}
			int[] m=new int[n.length-1];
			int j=0;
			int k=0;
			while(j<n.length)
			{
				if(j!=i)
					m[k++]=n[j++];
				else
					j++;
			}
			fill(m, f, result, level);
		}
	}
	static void sort(int[] n)
	{
		for(int i=1;i<n.length;i++)
			for(int j=n.length-1;j>=i;j--)
				if(n[j]<n[j-1])
				{
					int t=n[j];
					n[j]=n[j-1];
					n[j-1]=t;
				}
	}
	public static void main(String[] args)
	{
		int a=9461824;
		int b=a;
		level=1;
		while(b>9)
		{
			b/=10;
			level++;
		}
		int[] n=new int[level];
		b=a;
		for(int i=0;i<level;i++)
		{
			n[i]=b%10;
			b/=10;
		}
		sort(n);
		int[] f=new int[level+1];
		f[0]=1;
		for(int i=1;i<level+1;i++)
		{
			f[i]=f[i-1];
			f[i]*=i;
		}
		int[] result=new int[f[level]];
		count=0;
		fill(n, f, result, level);
		for(int i=0;i<count;i++)
			System.out.println(result[i]);
	}
}
