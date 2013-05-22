#include<iostream>
using namespace std;

bool is_leap(int i)
{
    if(i%4==0 && i%100!=0)
        return true;
    else if(i%400==0)
        return true;
    return false;
}