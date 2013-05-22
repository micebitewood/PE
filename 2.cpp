#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    long int a=1, b=2, c;
    unsigned long int sum=2;

    do
    {
        c=a+b;
        if(c%2==0)
            sum+=c;
        a=b;
        b=c;
    }
    while(c<4000000);
    ofstream fout;
    fout.open("test");
    fout << sum;
    fout.close();
}
