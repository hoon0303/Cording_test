#include<iostream>
using namespace std;

int main(void)
{
	int n, k;
	cin >> n;
	k = n;
	int cnt = 0;
	while (1)
	{
		cnt++;
		int x, y;
		x = n % 10;
		y = n / 10;
		int z = x + y;
		n = (n % 10) * 10 + z % 10;
		if (n == k)
			break;
	}
	cout << cnt;
}
