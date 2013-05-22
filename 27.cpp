#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool search(int* p, int l, int r, int i)
{
    int m=(l+r)/2;

    if(l==r && p[m]!=i)
        return false;
    if(p[m]==i)
        return true;
    if(p[m]>i)
        return search(p, 0, m, i);
    return search(p, m+1, r, i);
}

int main()
{
    ofstream fout;
    fout.open("test");
    ifstream fin;
    fin.open("prime");
    int p[78499];
    int count=0;
    while(!fin.eof())
        fin >> p[count++];
    int max=0;
    int product;
    for(int a=-999;a<999;a++)
    {
        for(int b=-999;b<999;b++)
        {
            int i=0;
            while(search(p, 0, count, i*i+a*i+b))
                i++;
            if(i>max)
            {
                max=i;
                product=a*b;
            }
        }
    }
    fout << product;
    fout.close();
}
