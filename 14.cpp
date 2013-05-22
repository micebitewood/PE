#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int i, max_count=0, max_n=999999, count;
    unsigned long int j;
    bool b[1000000];

    ofstream fout;
    fout.open("test");
    for(i=0;i<1000000;i++)
        b[i]=true;
    for(i=999999;i>0;i--)
    {
        if(b[i])
        {
            j=i;
            count=1;
            while(j!=1)
            {
                if(j%2==0)
                    j=j/2;
                else
                    j=j*3+1;
                if(j<1000000)
                    b[j]=false;
                count++;
            }
            if(max_count<count)
            {
                max_count=count;
                max_n=i;
            }
        }
    }
    fout << max_n;
    fout.close();
}
