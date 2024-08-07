#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

int main(void)
{
	map <string,int> rst;
	int n,r;
	vector<int> x;
	scanf("%d %d", &n, &r);
	for (int i = 0; i < n; i++)
	{
		x.push_back(i + 1);
	}
	do {
		int temp = 0;
		for (int i = 0; i < r; i++)
		{
			temp = temp * 10 + x[i];
		}
		if (rst[to_string(temp)] == 1)
			continue;
		for (int i = 0; i < r; i++)
		{
			printf("%d ", x[i]);
		}
		rst[to_string(temp)] = 1;
		printf("\n");
	} while (next_permutation(x.begin(), x.end()));

}
