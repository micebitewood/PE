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