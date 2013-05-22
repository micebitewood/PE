#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool check(unsigned long long result)
{
    if(result<1000000000)
        return false;
    int a=(result/1000000)%1000;
    int b=(result/100000)%1000;
    int c=(result/10000)%1000;
    int d=(result/1000)%1000;
    int e=(result/100)%1000;
    int f=(result/10)%1000;
    int g=result%1000;
    if(a%2==0 && b%3==0 && c%5==0 && d%7==0 && e%11==0 && f%13==0 && g%17==0)
        return true;
    return false;
}

void fill(unsigned long long* result, int* n, int c, int& count, int* f)
{
    if(c==1)
    {
        result[count]*=10;
        result[count]+=n[0];
        count++;
        return;
    }
    for(int i=0;i<c;i++)
    {
        result[count]*=10;
        result[count]+=n[i];
        int j;
        for(j=0;j<f[c-1];j++)
            result[count+j]=result[count];
        int* m=new int[c-1];
        j=0;
        int k=0;
        while(j<c)
        {
            if(j!=i)
                m[k++]=n[j++];
            else
                j++;
        }
        fill(result, m, c-1, count, f);
    }
}

int main()
{
    ifstream fin;
    ofstream fout;
    fout.open("test");
    fin.open("prime.txt");
    int* f=new int[11];
    int i;
    f[0]=1;
    for(i=1;i<11;i++)
        f[i]=f[i-1]*i;
    int* prime=new int[78498];
    i=0;
    while(!fin.eof())
        fin >> prime[i++];
    int* n=new int[10];
    for(i=0;i<10;i++)
        n[i]=i;
    unsigned long long* result=new unsigned long long[3628800];
    int count=0;
    fill(result, n, 10, count, f);
    unsigned long long sum=0;
    for(i=0;i<3628800;i++)
        if(check(result[i]))
        {
            fout << result[i] << endl;
            sum+=result[i];
        }
    fout << sum;
    delete[] prime;
    delete[] f;
    delete[] n;
    fout.close();
}
