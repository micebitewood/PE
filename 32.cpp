#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool share(int i, int j, int k)
{
    int n[9];
    int l=0;
    while(i>0)
    {
        n[l++]=i%10;
        i/=10;
    }
    while(j>0)
    {
        n[l++]=j%10;
        j/=10;
    }
    while(k>0)
    {
        n[l++]=k%10;
        k/=10;
    }
    for(i=0;i<9;i++)
        for(j=i+1;j<9;j++)
            if(n[i]==n[j] || n[i]==0)
                return true;
    return false;
}

int main()
{
    ofstream fout;
    fout.open("test");
    int i;
    int sum=0;
    bool f[10000];
    for(i=1000;i<10000;i++)
        f[i]=true;
    int j;
    for(i=2;i<9;i++)
        for(j=1234;j<10000;j++)
            if(i*j<10000)
            {
                int k=i*j;
                if(!share(i, j, k))
                    if(f[k])
                    {
                        sum+=k;
                        f[k]=false;
                    }
            }
    for(i=12;i<100;i++)
        for(j=123;j<1000;j++)
            if(i*j<10000)
            {
                int k=i*j;
                if(!share(i, j, k))
                    if(f[k])
                    {
                        sum+=k;
                        f[k]=false;
                    }
            }
    fout << sum;
    fout.close();
}
