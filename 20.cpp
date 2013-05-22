#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int a[1000], b[1000];
    int i, j, count=1, f, sum=0;;
    ofstream fout;
    fout.open("test");
    for(i=0;i<1000;i++)
    {
        a[i]=0;
        b[i]=0;
    }
    a[0]=1;
    for(i=2;i<101;i++)
    {
        j=0;
        while(j<count)
        {
            a[j]*=i;
            if(b[j]!=0)
            {
                a[j]+=b[j];
                b[j]=0;
            }
            b[j+1]=a[j]/10;
            a[j]%=10;
            j++;
        }
        while(b[count]!=0)
        {
            b[count+1]=b[count]/10;
            a[count]=b[count]%10;
            count++;
        }
    }
    for(i=999;i>=0;i--)
        if(a[i]!=0)
            sum+=a[i];
    fout << sum;
    fout.close();
}
