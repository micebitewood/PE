#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int rec(int i)
{
    int n[1000];
    int j=0;
    int k=1;
    while(k!=0)
    {
        k=k*10;
        n[j]=k;
        for(int l=0;l<j;l++)
            if(n[l]==k)
                return j-l;
        j++;
        k=k%i;
    }
    return 0;
}

int main()
{
    ofstream fout;
    fout.open("test");
    int max=0;
    int max_i;
    for(int i=2;i<1000;i++)
    {
        if(max<rec(i))
        {
            max=rec(i);
            max_i=i;
        }
    }
    fout << max_i;
    fout.close();
}
