#include<iostream>
#include<cstdio>
#include<stack>
#include<string>

using namespace std;

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		stack<char> stack;
		string x;
		cin >> x;
		for (int j = 0; j < x.size(); j++)
		{
			
			if (x[j] == '(')
			{
				stack.push(x[j]);
			}
			//cout << x[i]<<" "<<(x[i] == ')')<<endl;
			if (x[j] == ')')
			{
				if (stack.empty())
				{
					stack.push(')');
				}
				if (stack.top() == '(')
				{
					stack.pop();
				}
				
			}
		}
		if (stack.empty())
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
}