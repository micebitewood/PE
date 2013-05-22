#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test");
        int i, j;
        bool f[10];
        int n[10];
        long int total=1000000;
        long int temp;
        int count;
        long int count_max=1, count_min;
        for(i=0;i<10;i++)
        {
            f[i]=true;
            count_max*=(i+1);
        }
        for(i=10;i>0;i--)
        {
            count_min=count_max/i;
            temp=count_max;
            count=i;
            do
            {
                temp=temp-count_min;
                count--;
            }while(temp+1>total && count>=0);
            fout << temp << ' ' << total << ' ' << i-count << ' ' << 10-i << endl;
            for(j=9;j>=0;j--)
            {
                if(f[j])
                    count++;
                if(count==i)
                {
                    n[10-i]=j;
                    f[j]=false;
                    break;
                }
            }
            count_max/=i;
            total-=temp;
        }
        for(i=0;i<10;i++)
            fout << n[i];

    fout.close();
}
