#include<iostream>
#include<cmath>
#include"arrange.h"//void arrange(int* result, int* n, int level, int& count, int* f)
#include"gcd.h"//int gcd(int, int)
#include"is_leap.h"//bool is_leap(int)
#include"is_palindrome.h"//bool is_palindromic(unsigned long long) & bool is_palindrome(int*, int)
#include"is_prime.h"//bool is_prime(int)
#include"mergesort.h"//void MergeSort(int*, int, int)
#define MAX 101
using namespace std;

int min(int i, int j)
{
	if(i > j)
		return j;
	else
		return i;
}

int main()
{
	int s[MAX][MAX];
	int i, j;
	for(i = 1; i < MAX; i++)
		for(j = 1; j < MAX; j++)
			s[i][j] = 0;
	for(i = 1; i < MAX; i++)
		s[i][i] = 1;
	for(i = 1; i < MAX; i++)
		s[i][1] = 1;
	for(j = 2; j < MAX; j++)
	{
		for(i = j + 1; i < MAX; i++)
		{
			for(int k = 1; k <= min(i-j, j); k++)
			{
				s[i][j] += s[i-j][k];
			}
		}
	}
	unsigned long sum = 0;
	for(j = 1; j < 100; j++)
		sum += s[100][j];
	cout << sum << endl;
}
