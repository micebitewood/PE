#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_triangle(int n)
{
    n=n*2;
    int s=(int)sqrt(n);
    if(s*(s+1)==n)
        return true;
    return false;
}

int sum(string s)
{
    int i=0;
    int total=0;
    while(s[i]!=0)
    {
        total+=s[i]-'A'+1;
        i++;
    }
    return total;
}

int main()
{
    ifstream fin;
    ofstream fout;
    fout.open("test");
    fin.open("42.txt");
    string s;
    int count=0;
    while(!fin.eof())
    {
        fin >> s;
        if(is_triangle(sum(s)))
            count++;
    }
    fout << count;
    fout.close();
}
