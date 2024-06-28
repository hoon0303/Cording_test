#include <string>
#include <vector>
#include<iostream>

using namespace std;

int rst = 0;
int dfs(vector<int> numbers, int target, int i, int x) // dfs
{

	if (i == numbers.size())
	{
		if (target == x)
			rst++;
		return 1;
	}

	if (dfs(numbers, target, i + 1, x + numbers[i]))
	{

	}
	if (dfs(numbers, target, i + 1, x - numbers[i]))
	{

	}
	return -1;
}
int solution(vector<int> numbers, int target) {
	int answer = 0;
	dfs(numbers, target, 0, 0);
	answer = rst;
	return answer;
}