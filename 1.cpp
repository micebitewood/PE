#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int i=3;
    int sum=0;

    while(i<1000)
    {
        sum+=i;
        i+=3;
    }
    i=5;
    while(i<1000)
    {
        sum+=i;
        i+=5;
        while(i%3==0)
            i+=5;
    }
    ofstream fout;
    fout.open("test");
    fout << sum;
    fout.close();
}
