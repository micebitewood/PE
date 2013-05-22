#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test");
    int n[10]={3,3,4,8,2,0,0,0,0,0};
    bool f[11];
    for(int i=0;i<11;i++)
        f[i]=false;
    for(int i=0;i<7830457;i++)
    {
        for(int j=0;j<10;j++)
        {
            n[j]*=2;
            if(f[j])
            {
                f[j]=false;
                n[j]+=1;
            }
            if(n[j]>9)
            {
                f[j+1]=true;
                n[j]%=10;
            }
        }
    }
    for(int i=9;i>=0;i--)
        fout << n[i];
    fout.close();
}
