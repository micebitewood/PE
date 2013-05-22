#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_prime(int i)
{
    for(int k=2;k<sqrt(i);k++)
        if(i%k==0)
            return false;
    return true;
}
int main()
{
    unsigned long int n=600851475143;
    int i;

    for(i=sqrt(n);i>1;i--)
    {
        if(is_prime(i))
            if(n%i==0)
                break;
    }
    ofstream fout;
    fout.open("test");
    fout << i;
    fout.close();
}
