#include<iostream>
#include<fstream>
using namespace std;

int max_8(int* n, int i)
{
    int max, a, b;

    max=n[i]*n[i+1]*n[i+2];
    a=n[i+5]*n[i+6]*n[i+7];
    if(n[i+1]>=n[i+6])
        b=n[i+1]*n[i+2]*n[i+5];
    else
        b=n[i+2]*n[i+5]*n[i+5];
    if(max<a)
        max=a;
    if(max<b)
        max=b;
    max*=n[i+3]*n[i+4];
    return max;
}
int main()
{
    char c;
    int n[1000];
    int a, b, max, i;

    ofstream fout;
    ifstream fin;
    fin.open("8.txt");
    fout.open("test");
    for(i=0;i<1000;i++)
    {
        do
        {
            fin >> c;
        }while(c=='\n');
        n[i]=c-'0';
    }
    max=max_8(n, 0);
    for(i=1;i<124;i++)
    {
        a=max_8(n, i*8);
        b=max_8(n, i*8-4);
        if(max<a)
            max=a;
        if(max<b)
            max=b;
    }
    fout << max;
    fin.close();
    fout.close();
}
