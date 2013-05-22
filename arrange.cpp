#include<iostream>
#include<fstream>
#include<cmath>
#include"arrange.h"//void arrange(unsigned long long* result, int* n, int level, int& count, int* f)
#include"gcd.h"//int gcd(int, int)
#include"is_leap.h"//bool is_leap(int)
#include"is_palindrome.h"//bool is_palindromic(unsigned long long) & bool is_palindrome(int*, int)
#include"is_prime.h"//bool is_prime(int)
#include"mergesort.h"//void MergeSort(int*, int, int)
using namespace std;

int main()
{
    ofstream fout;
    fout.open("arr1-5");
    int n[5], f[6];
    f[0]=1;
    for(int i=0;i<5;i++)
    {
        f[i+1]=f[i]*(i+1);
        n[i]=i+1;
    }
    unsigned long long* result=new unsigned long long[120];
    int count=0;
    arrange(result, n, 5, count, f);
    for(int i=0;i<120;i++)
        fout << result[i] << endl;
    fout.close();
}
