#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int a[1000], b[1000], c[1000];
    int i, count, digits;
    bool f[1000];
    ofstream fout;
    fout.open("test");
    for(i=0;i<1000;i++)
    {
        a[i]=0;
        b[i]=0;
        c[i]=0;
        f[i]=false;
    }
    a[0]=1;
    b[0]=1;
    digits=1;
    count=2;
    while(digits<1000)
    {
        for(i=0;i<digits;i++)
        {
            c[i]+=a[i]+b[i];
            if(c[i]>9)
            {
                c[i+1]+=1;
                c[i]%=10;
            }
        }
        if(c[digits]!=0)
            digits++;
        for(i=0;i<digits;i++)
        {
            a[i]=b[i];
            b[i]=c[i];
            c[i]=0;
        }
        count++;
    }
    fout << count;
    fout.close();
}
