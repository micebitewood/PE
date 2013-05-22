#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_prime(int i, int* n, int count)
{
    int j;

    for(j=0;j<count;j++)
    {
        if(i%n[j]==0)
            break;
    }
    if(j<count)
        return false;
    n[count]=i;
    return true;
}

int main()
{
    int n[10001], count=1, i=3;
    ofstream fout;
    fout.open("test");

    n[0]=2;
    fout << '2' << endl;
    while(count<10001)
    {
        if(is_prime(i, n, count))
        {
            fout << i << endl;
            count+=1;
        }
        i+=2;
    }
    fout.close();
}
