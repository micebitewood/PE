#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;


bool is_palindromic(int n)
{
    int i=n;
    int s=0;

    while(i!=0)
    {
        int t=i%10;
        s*=10;
        s+=t;
        i=i/10;
    }
    if(s==n)
        return true;
    return false;
}
int main()
{
    ofstream fout;
    fout.open("test");
    int n, m;

    for(int i=1;i<=76;i++)
    {
        for(int j=1;j<=i;j++)
        {
            n=(1000-i)*(1000-j);
            if(is_palindromic(n))
            {
                for(int k=j-1;k>0;k--)
                    for(int l=i+1;(1000-k)*(1000-l)>n;l++)
                    {
                        m=(1000-k)*(1000-l);
                        if(is_palindromic(m))
                            n=m;
                    }
                fout << n;
                fout.close();
                return 0;
            }
        }
    }
}
