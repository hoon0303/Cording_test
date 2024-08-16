#include<iostream>
using namespace std;
int fact(int n)
{
	if (n < 1)
		return 1;
	return fact(n - 1)*n;
}
int main(void)
{
	int x;
	cin >> x;
	cout << fact(x);
	return 0;
}
