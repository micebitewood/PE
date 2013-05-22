#include<iostream>
using namespace std;

int main()
{
	char a = 'a';
	while (a <= 'z')
	{
		cout << a << char(a^79) << endl;
		a++;
	}
	return 0;
}
