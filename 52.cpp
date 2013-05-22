#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

void Merge(int* a, int l, int m, int r)
{
    int i=l;
    int j=m+1;
    int* b=new int[r-l+1];

    int k=0;
    while(i<=m && j<=r)
    {
        if(a[i]<=a[j])
            b[k++]=a[i++];
        else
            b[k++]=a[j++];
    }
    if(i>m)
        while(k<r-l+1)
            b[k++]=a[j++];
    else
        while(k<r-l+1)
            b[k++]=a[i++];
    for(int i=0;i<r-l+1;i++)
        a[l+i]=b[i];
}

void MergeSort(int* a, int l, int r)
{
    if(l==r)
        return;
    int m=(l+r)/2;
    MergeSort(a, l, m);
    MergeSort(a, m+1, r);
    Merge(a, l, m, r);
}

bool same_digit(int i, int j)
{
    int k=i;
    int level_i=0;
    int a[100], b[100];
    int l=0;
    while(k>0)
    {
        a[level_i++]=k%10;
        k/=10;
    }
    k=j;
    int level_j=0;
    while(k>0)
    {
        b[level_j++]=k%10;
        k/=10;
    }
    if(level_i!=level_j)
        return false;
    else
    {
        MergeSort(a, 0, level_i-1);
        MergeSort(b, 0, level_j-1);
        for(int k=0;k<level_i;k++)
            if(a[k]!=b[k])
                return false;
        return true;
    }
}

bool same(int i, int n)
{
    int k=i;
    for(int j=1;j<n;j++)
    {
        if(same_digit(k, k+i))
            k+=i;
        else
            return false;
    }
    return true;
}

int main()
{
    ofstream fout;
    fout.open("test");
    int i=10;
    while(true)
    {
        if(same(i, 6))
            break;
        i++;
    }
    fout << i;
    fout.close();
}
