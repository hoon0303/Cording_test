#include<iostream>
#include<vector>
using namespace std;

int main(void)
{
	int n, m;
	cin >> n >> m;
	vector<int> x;

	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		x.push_back(temp);
	}
	int cnt = 0;
	for (int i = x.size() - 1; i >= 0; i--)
	{
		if (m == 0)
			break;
		if (m / x[i] != 0)
		{
			cnt = m / x[i] + cnt;
			m = m % x[i];
		}
	}
	cout << cnt;
}
