#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int t[4], a, b, min;
    ofstream fout;

    fout.open("test");
    t[3]=333;
    for(a=499;a>2;a--)
    {
        t[0]=1000-a;
        t[1]=1000-2*a;
        t[2]=a;
        min=t[0]/2;
        for(int i=1;i<4;i++)
            if(min>t[i])
                min=t[i];
        for(b=min;b<a && b>0;b--)
            if(b*t[0]==500*t[1])
            {
                fout << a*b*(1000-a-b);
                fout.close();
                return 0;
            }
    }
}
