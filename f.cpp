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
    fout.open("fun_num");
    fout << "0: 1" << endl;
    int total=1;
    for(int i=1;i<11;i++)
    {
        total*=i;
        fout << i << ": " << total << endl;
    }
    fout.close();
}
