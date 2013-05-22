#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    unsigned long int sum=1;
    for(int i=2;i<21;i++)
    {
        if(sum%i!=0)
        {
            for(int j=2;j<i;j++)
                if(i%j==0)
                    while(sum%j==0)
                        sum/=j;
            sum*=i;
        }
    }
    ofstream fout;
    fout.open("test");
    fout << sum;
    fout.close();
}
