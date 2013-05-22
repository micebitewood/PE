#include<iostream>
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