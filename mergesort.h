#include<iostream>
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