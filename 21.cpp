#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int sum_d(int s)
{
    int m=1;
    int k=sqrt(s);

    for(int i=2;i<k+1;i++)
    {
        if(s%i==0)
        {
            m+=i;
            m+=(s/i);
        }
    }
    if(s==k*k)
        m-=k;
    return m;
}
int main()
{
    bool b[10000];
    int i, s, t;
    ofstream fout;
    fout.open("test");
    for(i=0;i<10000;i++)
        b[i]=true;
    for(i=0;i<4;i++)
        b[i]=false;
    for(i=4;i<10000;i++)
    {
        if(b[i])
        {
            s=sum_d(i);
            if(s==i)
                b[i]=false;
            else
            {
                t=sum_d(s);
                if(t!=i)
                {
                    b[i]=false;
                    if(s>i && s<10000)
                        b[s]=false;
                }
            }
        }
    }
    int r=0;
    for(i=4;i<10000;i++)
        if(b[i])
        {
            fout << i << ' ';
            r+=i;
        }
    fout << endl << r;
    fout.close();
}
