#include<iostream>
#include<fstream>
#include<cmath>
#include"arrange.h"//void arrange(int* result, int* n, int level, int& count, int* f)
#include"gcd.h"//int gcd(int, int)
#include"is_leap.h"//bool is_leap(int)
#include"is_palindrome.h"//bool is_palindromic(unsigned long long) & bool is_palindrome(int*, int)
#include"is_prime.h"//bool is_prime(int)
#include"mergesort.h"//void MergeSort(int*, int, int)
using namespace std;

int main()
{
    ofstream fout;
    fout.open("test.txt");
	ifstream fin;
	fin.open("59.txt");
	char c[3]={'g', 'o', 'd'};
	int i;
	int j;
	char ch;
	int sum = 0;
		j = 0;
		while(!fin.eof())
		{
			fin >> i;
			if(fin.eof())
				break;
			ch = i;
			ch ^= c[j];
			sum += ch;
			j++;
			j = j % 3;
		}
		fout << sum;
	/*
			while(c[2] <= 'z')
			{
				fin.clear();
				fin.seekg(0, ios::beg);
				j = 0;
				while(!fin.eof())
				{
					fin >> i;
					ch = i;
					ch ^= c[j];
					if(j==0)
						fout << ch;
					j++;
					j = j % 3;
				}
				c[2]++;
				fout << endl << endl;
			}*/
    fout.close();
}
