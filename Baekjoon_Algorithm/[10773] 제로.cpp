#include<iostream>
#include<cstdio>
#include<stack>

using namespace std;

int main(void)
{
	int k;
	stack<int> stack;
	scanf("%d", &k);
	for (int i = 0; i < k; i++)
	{
		int x;
		scanf("%d", &x);
		if (x == 0)
		{
			if (stack.empty())
			{
				continue;
			}
			else
			{
				stack.pop();
				continue;
			}
		}
		stack.push(x);
	}
	int sum = 0;
	while (!stack.empty())
	{
		sum = sum + stack.top();
		stack.pop();
	}
	printf("%d", sum);
	return 0;
}
