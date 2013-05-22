#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int a[1000];
    int i, j, b;
    bool f[1000];
    int count=1;
    int sum=0;

    ofstream fout;
    fout.open("test");
    for(i=0;i<1000;i++)
    {
        a[i]=0;
        f[i]=false;
    }
    a[0]=1;
    for(i=0;i<1000;i++)
    {
        j=0;
        while(j<count)
        {
            a[j]*=2;
            b=a[j]/10;
            if(b!=0)
                f[j+1]=true;
            a[j]%=10;
            if(f[j])
            {
                a[j]+=1;
                f[j]=false;
            }
            j++;
        }
        if(f[count])
        {
            a[count]+=1;
            f[count]=false;
            count++;
        }
    }
    for(i=999;i>=0;i--)
        if(a[i]!=0)
            sum+=a[i];
    fout << sum;
    fout.close();
}
