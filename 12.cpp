#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int ct(int n)
{
    int count=2;
    for(int i=2;i<n/2+1;i++)
    {
        if(n%i==0)
            count++;
    }
    return count;
}
int main()
{
    int count=0;
    int a, b;
    bool flag;
    ofstream fout;
    fout.open("test");
    a=2001;
    b=1000;
    while(count<500)
    {
        b++;
        if(ct(a)>ct(a+2))
        {
            count=ct(a)*ct(b);
            a+=2;
            flag=true;
        }
        else
        {
            a+=2;
            count=ct(a)*ct(b);
            flag=false;
        }
    }
    if(flag)
        a-=2;
    fout << a*b;
    fout.close();
}
