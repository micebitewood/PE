#include<iostream>
using namespace std;

bool is_palindrome(int* n, int max)
{
	int k=max/2;
	for(int i=0;i<=k;i++)
		if(n[i]!=n[max-i])
			return false;
	return true;
}

void addreverse(int* n, int& max)
{
	int* m=new int[max];
	for(int i=0;i<=max;i++)
	{
		m[i]=n[max-i]+n[i];
	}
	for(int i=0;i<=max;i++)
		n[i]=m[i];
	for(int i=0;i<max;i++)
	{
		if(n[i]>9)
		{
			n[i+1]+=1;
			n[i]-=10;
		}
	}
	if(n[max]>9)
	{
		n[max]-=10;
		max++;
		n[max]=1;
	}
}

void main()
{
	int n[60];

	int count=0;
	for(int i=1;i<10000;i++)
	{
		n[0]=i;
		int j=0;
		while(n[j]>9)
		{
			n[j+1]=n[j]/10;
			n[j]%=10;
			j++;
		}
		for(int k=0;k<49;k++)
		{
			addreverse(n, j);//n[j] is not 0;
			if(j!=0 && is_palindrome(n, j))
			{
				count++;
				break;
			}
		}
	}
	cout << 9999-count;
	getchar();
}