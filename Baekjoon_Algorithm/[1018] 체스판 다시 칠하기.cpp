#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int map[51][51] = { 0 };
vector<int> rst;
void F(int x, int y, int TRUE)
{
	int cnt = 0;
	for (int i = x; i < x + 8; i++)
	{
		for (int j = y; j < y + 8; j++)
		{
			
			if (TRUE == 0 && map[i][j] == 1)
			{
				cnt++;
			}
			if (TRUE == 1 && map[i][j] == 0)
			{
				cnt++;
			}
			TRUE = (TRUE + 1) % 2;
		}
		
		TRUE = (TRUE + 1) % 2;
	}
	rst.push_back(cnt);
}
int main(void)
{
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			char temp;
			cin >> temp;
			if (temp == 'W')
			{
				map[i][j] = 0;
			}
			if (temp == 'B')
			{
				map[i][j] = 1;
			}

		}
	}
	
	for (int i = 0; i <= n - 8; i++)
	{
		for (int j = 0; j <= m - 8; j++)
		{
			F(i, j,0);
			F(i, j, 1);
		}
	}
	sort(rst.begin(), rst.end());
	cout << rst[0];
	
}