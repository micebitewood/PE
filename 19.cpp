#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

bool is_leap(int i)
{
    if(i%4==0 && i%100!=0)
        return true;
    else if(i%400==0)
        return true;
    return false;
}

int main()
{
    int days[12]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    ofstream fout;
    fout.open("test");
    int count=366%7;
    int c=0;
    for(int i=1901;i<2001;i++)
    {
        for(int j=0;j<12;j++)
        {
            if(count==0)
                c++;
            count=(count+days[j])%7;
            if(j==1 && is_leap(i))
                count=(count+1)%7;;
        }
    }
    fout << c << endl;
    fout.close();
}
