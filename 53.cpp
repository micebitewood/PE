#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test");
    unsigned long long a[100], b[100];
    a[0]=1;
    a[1]=1;
    unsigned int sum=0;
    for(int i=2;i<=100;i++)
    {
        for(int j=1;j<i;j++)
            b[j]=a[j-1]+a[j];
        b[0]=1;
        b[i]=1;
        for(int j=0;j<=i;j++)
        {
            if(b[j]>1000000)
                sum++;
            a[j]=b[j];
        }
    }
    fout << sum;
    fout.close();
}
