#include <string>
#include <vector>
#include<iostream>
#include<map>

using namespace std;

int solution(vector<vector<string>> clothes)
{
	int answer = 1;
	map<string, int> x;
	vector<string> y;

	for (int i = 0; i < clothes.size(); i++)
	{
		if (x[clothes[i][1]] == 0)
		{
			y.push_back(clothes[i][1]);
		}
		x[clothes[i][1]]++;
	}
	for (int i = 0; i < y.size(); i++)
	{
		answer = answer* (x[y[i]] + 1);
	}
	return answer - 1;
}