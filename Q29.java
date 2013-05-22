import java.util.*;
public class Q29 {
	public static void main(String args[])
    {
        Set<String> hs=new HashSet<String>();
        int[] n=new int[202];
        int[] f=new int[202];
        String s="";
        final int max=100;
        for(int i=2;i<=max;i++)
        {
        	for(int k=0;k<200;k++)
            {
                n[k]=0;
                f[k]=0;
            }
            int l=0;
            n[l]=i;
            int count=1;
            while(n[l]>9)
            {
                n[l+1]=n[l]/10;
                n[l]%=10;
                l++;
                count++;
            }
            for(int j=2;j<=max;j++)
            {
                l=0;
                while(l<count)
                {
                    n[l]*=i;
                    if(f[l]!=0)
                    {
                        n[l]+=f[l];
                        f[l]=0;
                        f[l]=0;
                    }
                    if(n[l]>9)
                    {
                        f[l+1]=n[l]/10;
                        n[l]%=10;
                    }
                    l++;
                }
                while(f[l]>0)
                {
                    f[l+1]=f[l]/10;
                    n[l]=f[l]%10;
                    f[l]=0;
                    count++;
                    l++;
                }
                s="";
                for(int k=199;k>=0;k--)
                    s+=n[k]+"";
                hs.add(s);
            }
        }
        Iterator<String> it=hs.iterator();
        int count=0;
        while(it.hasNext())
            count++;
        System.out.print(count);
    }
}
