#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test");
    int max=0;
    int max_p;
    int p;
    for(p=12;p<=1000;p++)
    {
        int count=0;
        for(int a=p/3+1;a<p;a++)
        {
            for(int b=(p-a)/2+1;b<p-a;b++)
            {
                if((p-a-b)*(p-a-b)==(a+b)*(a-b))
                    count++;
            }
        }
        if(max<count)
        {
            max=count;
            max_p=p;
        }
    }
    fout << max << ' ' << max_p;
    fout.close();
}
