#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test");
    int i;
    unsigned long int sum=1;
    for(i=40;i>20;i--)
    {
        sum*=i;
    }
    for(i=20;i>0;i--)
    {
        sum=sum/i;
    }
    fout << sum;
    fout.close();
}
