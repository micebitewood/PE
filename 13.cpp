#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int n[100][50];
    int sum[53];
    int i, j;
    char c;

    ifstream fin;
    ofstream fout;
    fout.open("test");
    fin.open("13.txt");
    for(i=0;i<100;i++)
    {
        for(j=49;j>=0;j--)
        {
            do
            {
                fin >> c;
            }while(c=='\n');
            n[i][j]=c-'0';
        }
    }
    for(i=0;i<53;i++)
        sum[i]=0;
    i=0;
    do
    {
        if(i<50)
            for(j=0;j<100;j++)
            {
                sum[i]+=n[j][i];
            }
        sum[i+1]=sum[i]/10;
        sum[i]=sum[i]%10;
        i++;
    }while(sum[i]!=0 || i<50);
    for(j=i-1;j>i-11;j--)
        fout << sum[j];
    fout.close();
}
