#include<iostream>
using namespace std;

void arrange(unsigned long long* result, int* n, int c, int& count, int* f)
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
        arrange(result, m, c-1, count, f);
    }
}