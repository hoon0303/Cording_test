#include<iostream>
#include<string>
#include<stack>
#include<cstdio>

using namespace std;

int main(void)
{
	stack<int> stack;
	string temp;
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		if (temp == "push")
		{
			int x;
			scanf("%d", &x);
			stack.push(x);
		}
		if (temp == "pop")
		{
			if (stack.empty())
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", stack.top());
				stack.pop();
			}
		}
		if (temp == "size")
		{
			printf("%d\n", stack.size());
		}
		if (temp == "empty")
		{
			printf("%d\n", stack.empty());
		}
		if (temp == "top")
		{
			if (stack.empty())
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", stack.top());
			}
		}
	}
	return 0;
}
