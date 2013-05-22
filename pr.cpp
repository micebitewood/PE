#include<iostream>
#include<fstream>
#include<cmath>
#define MAX 1000000
using namespace std;

bool is_prime(unsigned long long i)
{
    unsigned long long j=sqrt(i)+1;
    unsigned long long k;
    for(k=2;k<j;k++)
        if(i%k==0)
            return false;
    return true;
}

int main()
{
    ofstream fout;
    fout.open("prime.txt");
    unsigned long long i;
    unsigned long long j;
    bool* f=new bool[MAX];
    for(i=2;i<MAX;i++)
        f[i]=true;
    for(i=2;i<MAX/2+1;i++)
    {
        if(f[i])
        {
            if(!is_prime(i))
            {
                f[i]=false;
            }
            j=i+i;
            while(j<MAX)
            {
                f[j]=false;
                j+=i;
            }
        }
    }
    int count=0;
    for(i=2;i<MAX;i++)
        if(f[i])
            count++;
    fout << count << endl;
    for(i=2;i<MAX;i++)
        if(f[i])
            fout << i << endl;
    delete[] f;
    fout.close();
}
