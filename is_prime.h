#include<iostream>
#include<cmath>
using namespace std;

bool is_prime(int i)
{
	int j=sqrt(i)+1;
    for(int k=2;k<j;k++)
        if(i%k==0)
            return false;
    return true;
}