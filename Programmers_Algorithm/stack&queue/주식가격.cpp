#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;
	for (int i = 0; i<prices.size(); i++)
	{
		if (i == prices.size() - 1)
		{
			answer.push_back(0);
			break;
		}
		int temp = 0;
		for (int j = i; j<prices.size(); j++)
		{
			if (prices[i]>prices[j])
			{
				temp = j - i;
				break;
			}
		}
		if (temp == 0)
			temp = prices.size() - i - 1;
		answer.push_back(temp);

	}
	return answer;
}