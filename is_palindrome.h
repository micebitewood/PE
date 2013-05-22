#include<iostream>
#include<fstream>
using namespace std;

bool is_palindromic(unsigned long long n)
{
    unsigned long long i=n;
    unsigned long long s=0;

    while(i!=0)
    {
        int t=i%10;
        s*=10;
        s+=t;
        i=i/10;
    }
    if(s==n)
        return true;
    return false;
}

bool is_palindrome(int* n, int max)
{
	int k=max/2;
	for(int i=0;i<=k;i++)
		if(n[i]!=n[max-i])
			return false;
	return true;
}