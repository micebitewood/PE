#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_prime(unsigned long long n)
{
    unsigned long long i=sqrt(n)+1;
    unsigned long long j;

    if(n%2!=0)
    {
        for(j=3;j<i;j+=2)
        {
            if(n%j==0)
                return false;
        }
    }
    else
        return false;
    return true;
}

bool share(unsigned long long n)
{
    unsigned long long i=n;
    int a[9];
    int j=0;
    while(i>0)
    {
        a[j++]=i%10;
        i/=10;
    }
    for(i=0;i<j;i++)
        for(int k=i+1;k<j;k++)
            if(a[i]==a[k] || a[i]==0)
                return true;
    return false;
}

void fill(unsigned long long* a, int* f, int* n, int max)
{
    if(max==1)
    {
        a[count]*=10;
        a[count]+=n[0];
        count++;
        return;
    }
    for(int i=0;i<max;i++)
    {
        a[count]*=10;
        a[count]+=n[i];
        for(int j=0;j<f[
    }
}

int main()
{
    ofstream fout;
    fout.open("test");
    int n[9]={1, 2, 3, 4, 5, 6, 7, 8, 9};
    int f[10]={1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    unsigned long long a[362880];
    fill(a, f, n, 9);
        if(!share(n))
            if(is_prime(n))
            {
                fout << n;
                break;
            }
    fout.close();
}
