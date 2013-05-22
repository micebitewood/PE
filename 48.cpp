#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int n[1000][11];
    int i, j, k;
    int count;
    int f[11];
    ofstream fout;
    fout.open("test");
    for(i=0;i<1000;i++)
    {
        n[i][0]=1;
        for(j=1;j<11;j++)
        {
            n[i][j]=0;
        }
    }
    for(i=0;i<11;i++)
        f[i]=0;
    for(i=0;i<1000;i++)
    {
        count=1;
        for(k=0;k<=i;k++)
        {
            j=0;
            while(j<count)
            {
                n[i][j]*=(i+1);
                if(f[j]!=0)
                {
                    n[i][j]+=f[j];
                    f[j]=0;
                }
                if(n[i][j]>9)
                {
                    f[j+1]=n[i][j]/10;
                    n[i][j]%=10;
                }
                j++;
            }
            if(f[count]!=0 && count<10)
            {
                while(f[count]>0 && count<10)
                {
                    f[count+1]+=f[count]/10;
                    n[i][count]=f[count]%10;
                    f[count]=0;
                    count++;
                }
            }
        }
    }
    for(j=0;j<10;j++)
        f[j]=0;
    for(i=0;i<10;i++)
    {
        for(j=0;j<1000;j++)
        {
            f[i]+=n[j][i];
        }
        if(f[i]>9)
        {
            f[i+1]+=(f[i]/10);
            f[i]=f[i]%10;
        }
    }
    for(i=9;i>=0;i--)
        fout << f[i];
    fout.close();
}
