#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    int i;
    int n[5050], m[5050];
    fout.open("test");
    fin.open("67.txt");
    for(i=0;i<5050;i++)
    {
        fin >> n[i];
    }
    m[0]=n[0];
    int level=1;
    int count=0;
    for(i=1;i<5050;i++)
    {
        m[i]=n[i];
        if(count>0 && count<level)
        {
            if(m[i-level-1]>=m[i-level])
                m[i]+=m[i-level-1];
            else
                m[i]+=m[i-level];
        }
        else if(count==0)
        {
            m[i]+=m[i-level];
        }
        else
        {
            m[i]+=m[i-level-1];
        }
        count++;
        if(count>level)
        {
            level++;
            count=0;
        }
    }
    int max=m[4950];
    for(i=4951;i<5050;i++)
    {
        if(max<m[i])
            max=m[i];
    }
    fout << max;
    fout.close();
}
