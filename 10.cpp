#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_prime(int i)
{
    for(int j=2;j<sqrt(i);j++)
        if(i%j==0)
            return false;
    return true;
}
int main()
{
    bool b[2000001];
    unsigned long int sum=0;

    ofstream fout;
    fout.open("test1");
    for(int i=2;i<2000001;i++)
    {
        b[i]=true;
    }
    for(int i=2;i<1000001;i++)
    {
        if(b[i]==true)
        {
            int j=i+i;
            while(j<2000001)
            {
                b[j]=false;
                j+=i;
            }
        }
    }
    for(int i=2;i<2000001;i++)
        if(b[i]==true)
            sum+=i;
    fout << sum;
    fout.close();
}
