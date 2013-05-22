#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int gcd(int a, int b)
{
    if(a==0 || b==0)
        return 1;
    else
    {
        int c;
        while(a!=0)
        {
            c=b%a;
            b=a;
            a=c;
        }
        return b;
    }
}

void simplify(int& a, int& b)
{
    int c=gcd(a, b);//a<=b
    a=a/c;
    b=b/c;
    return;
}

bool same(int a, int b, int c, int d)
{
    simplify(a, b);
    simplify(c, d);
    if(a==c && b==d)
        return true;
    return false;
}

int main()
{
    ofstream fout;
    fout.open("test");
    int numerator=1;
    int denometor=1;
    for(int i=11;i<100;i++)
    {
        for(int j=10;j<i;j++)
        {
            bool flag=false;
            if(j%10==i%10 && j%10!=0)
                if(same(j/10, i/10, j, i))
                    flag=true;
            if(j/10==i%10)
                if(same(j%10, i/10, j, i))
                    flag=true;
            if(j%10==i/10)
                if(same(j/10, i%10, j, i))
                    flag=true;
            if(j/10==i/10)
                if(same(j%10, i%10, j, i))
                    flag=true;
            if(flag==true)
            {
                numerator*=j;
                denometor*=i;
            }
        }
    }
    simplify(numerator, denometor);
    fout << denometor;
    fout.close();
}
