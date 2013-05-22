#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

void comp(int* a,int i, int n, int& count)
{
    if(i==1 || n==0)
    {
        count++;
        return;
    }
    int j=0;
    while(j<=n)
    {
        comp(a, i-1, n-j, count);
        j+=a[i-1];
    }
}

int main()
{
    ofstream fout;
    fout.open("test");
    int a[8]={1, 2, 5, 10, 20, 50, 100, 200};
    int count=0;
    comp(a, 8, 200, count);
    fout << count;
    fout.close();
}
