#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool search(int* a, int l, int r, int n)
{
    if(l==r)
        if(a[l]!=n)
            return false;
    int m=(l+r)/2;
    if(a[m]==n)
        return true;
    else if(a[m]>n)
        return search(a, l, m, n);
    else
        return search(a, m+1, r, n);
}

int main()
{
    ofstream fout;
    fout.open("test");
    ifstream fin;
    fin.open("prime");
    int a[78500];
    int total=0;
    while(!fin.eof())
    {
        fin >> a[total++];
    }
    int count=0;
    int i=11;
    int sum=0;
    while(count<11)
    {
        if(search(a, 0, total, i))
        {
            int j=i;
            int level=1;
            bool flag=true;
            while(j>9)
            {
                j/=10;
                level*=10;
                if(!search(a, 0, total, j))
                    flag=false;
            }
            j=i;
            while(level>9)
            {
                j=j%level;
                level/=10;
                if(!search(a, 0, total, j))
                        flag=false;
            }
            if(flag)
            {
                count++;
                sum+=i;
            }
        }
        i+=2;
    }
    fout << sum;
    fout.close();
}
