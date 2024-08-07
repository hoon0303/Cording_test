#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;

int main(void)
{
	map<string, int> check;
	int n, m;
	scanf("%d %d", &n, &m);
	vector<int> x;
	for (int i = 0; i < n; i++)
	{
		x.push_back(i + 1);
	}
	do {
		string temp = "";
		for (int i = 0; i < m; i++)
		{
			temp = temp + to_string(x[i]);
		}
		sort(temp.begin(), temp.end());
		if (check[temp])
		{
			continue;
		}
		for (int i = 0; i < m; i++)
		{
			cout << x[i] << " ";
		}
		
		check[temp] = 1;
		cout << endl;
	} while (next_permutation(x.begin(), x.end()));
}
