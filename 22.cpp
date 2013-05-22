#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

void sort(string* n, int num)
{
    string m[26][5163], temp;
    int count[26], i, j;
    int sum=0;

    for(i=0;i<26;i++)
        count[i]=0;
    for(i=0;i<num;i++)
    {
        j=n[i][0]-'A';
        m[j][count[j]]=n[i];
        count[j]++;
    }
    for(i=0;i<26;i++)
    {
        for(j=0;j<count[i];j++)
        {
            for(int k=count[i]-1;k>j;k--)
            {
                int l=1;
                while(m[i][k][l]==m[i][k-1][l])
                    l++;
                if(l==m[i][k].length() || m[i][k][l]<m[i][k-1][l])
                {
                    temp=m[i][k];
                    m[i][k]=m[i][k-1];
                    m[i][k-1]=temp;
                    l--;
                }
            }
            n[j+sum]=m[i][j];
        }
        sum+=count[i];
    }
    if(sum!=num)
        cout << "error" << endl;
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("22.txt");
    fout.open("test");
    int i=0;
    string n[5163];
    while(!fin.eof())
        fin >> n[i++];
    unsigned long int value[5163];
    sort(n, i);
    int j;
    for(j=0;j<i;j++)
    {
        fout << n[j] << endl;
    }
    for(j=0;j<i;j++)
    {
        int k=0;
        value[j]=0;
        while(n[j][k]!=0)
        {
            value[j]+=(n[j][k]-'A'+1);
            k++;
        }
        value[j]*=(j+1);
    }
    unsigned long int sum=0;
    for(j=0;j<i;j++)
        sum+=value[j];
    fout << sum;
    fin.close();
    fout.close();
}
