#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    unsigned long int sum1=0, sum2=0;
    for (int i=1;i<101;i++)
    {
        sum1+=i*i;
        sum2+=i;
    }
    sum2=sum2*sum2;
    ofstream fout;
    fout.open("test");
    fout << sum2-sum1;
    fout.close();
}
