#include<iostream>
using namespace std;
int fact(int n)
{
	if (n == 0)
		return 0;
	if (n == 1)
		return 1;
	return fact(n - 1)+fact(n-2);
}
int main(void)
{
	int x;
	cin >> x;
	cout << fact(x);
	return 0;
}
