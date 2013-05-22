#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    int m[20][20];
    int i, j, max=1, sum, k;
    ofstream fout;
    ifstream fin;
    fin.open("11.txt");
    fout.open("test");
    for(i=0;i<20;i++)
        for(j=0;j<20;j++)
            fin >> m[i][j];
    for(k=0;k<4;k++)
        max*=m[0][k];
    for(i=0;i<20;i++)
    {
        for(j=0;j<20;j++)
        {
            if(j<17)
            {
                sum=1;
                for(k=0;k<4;k++)
                    sum*=m[i][j+k];
                if(max<sum)
                    max=sum;
            }
            if(i<17)
            {
                sum=1;
                for(k=0;k<4;k++)
                    sum*=m[i+k][j];
                if(max<sum)
                    max=sum;
            }
            if(i<17 && j<17)
            {
                sum=1;
                for(k=0;k<4;k++)
                    sum*=m[i+k][j+k];
                if(max<sum)
                    max=sum;
            }
            if(i<17 && j>2)
            {
                sum=1;
                for(k=0;k<4;k++)
                    sum*=m[i+k][j-k];
                if(max<sum)
                    max=sum;
            }
        }
    }
    fout << max;
    fout.close();
}
