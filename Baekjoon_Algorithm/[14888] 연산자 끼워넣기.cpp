#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector<int> result;
void dfs(vector<int> num, int x, int y, int z, int k, int index, int rst)
{
	if (n == index)
	{
		result.push_back(rst);
		return;
	}
	if (x > 0)
	{
		dfs(num, x - 1, y, z, k, index + 1, rst + num[index]);
	}
	if (y > 0)
	{
		dfs(num, x , y-1, z, k, index + 1, rst - num[index]);
	}
	if (z > 0)
	{
		dfs(num, x , y, z-1, k, index + 1, rst * num[index]);
	}
	if (k > 0)
	{
		dfs(num, x , y, z, k-1, index + 1, rst / num[index]);
	}
}
int main(void)
{
	vector<int> num;
	int x, y, z, k;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int temp;
		cin >> temp;
		num.push_back(temp);
	}
	cin >> x >> y >> z >> k;
	
	dfs(num, x, y, z, k, 1, num[0]);
	sort(result.begin(), result.end());
	cout << result.back() << endl;
	cout << result[0];
	return 0;

}
