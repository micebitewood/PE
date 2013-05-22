#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool search(int* n, int l, int r, int t)
{
    int m=(l+r)/2;

    if(l==r)
        if(n[m]==t)
            return true;
        else
            return false;
    if(t<n[m])
        return search(n, l, m, t);
    else if(t==n[m])
        return true;
    return search(n, m+1, r, t);
}

int main()
{
    ifstream fin;
    fin.open("prime.txt");
    ofstream fout;
    fout.open("test");
    int max_num;
    fin >> max_num;
    int i=0;
    int* n=new int[max_num];
    while(!fin.eof())
        fin >> n[i++];
    int sum;
    int max=0;
    int max_count=0;
    for(i=0;i<max_num;i++)
    {
        sum=n[i];
        int j=i+1;
        do
        {
            if(search(n, 0, max_num, sum))
                if(max_count<j-i)
                {
                    max=sum;
                    max_count=j-i;
                }
            sum+=n[j++];
        }while(sum<1000000);
    }
    fout << max;
    delete[] n;
    fin.close();
    fout.close();
}
