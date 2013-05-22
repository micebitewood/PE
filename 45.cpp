#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_hex(unsigned long long n)
{
    unsigned long long k=sqrt(n*2);
    k++;
    k/=2;
    if(k*(2*k-1)==n)
        return true;
    return false;
}

bool is_pen(unsigned long long n)
{

    unsigned long long k=sqrt(n*6);
    k++;
    k/=3;
    if((k*(3*k-1))/2==n)
        return true;
    return false;
}

int main()
{
    ofstream fout;
    fout.open("test");
    unsigned long long i=286;
    unsigned long long n=(i*i+i)/2;
    while(!is_pen(n) || !is_hex(n))
    {
        i++;
        n=(i*i+i)/2;
    }
    fout << n;
    fout.close();
}
