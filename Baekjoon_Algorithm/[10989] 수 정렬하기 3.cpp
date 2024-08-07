#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

int m[10001] = { 0 };
int main(void)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int x;
		scanf("%d", &x);
		m[x]++;
	}
	int cnt = 0;
	for (int i = 1; i <= 10000; i++)
	{
		if (cnt > n)
			break;
		
		for (int j = 0; j < m[i]; j++)
		{
			printf("%d\n", i);
			cnt++;
		}
		
	}
}
