#include <string>
#include <vector>
#include <iostream>
#include <utility>

using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	vector<pair<int, int>> index;
	for (int i = 0; i < priorities.size(); i++)
	{
		index.push_back(make_pair(priorities[i], i));
	}

	for (int i = 0; i < priorities.size(); i++)
	{
		for (int j = i + 1; j < priorities.size(); j++)
		{
			if (index[i].first < index[j].first)
			{
				index.push_back(index[i]);
				index.erase(index.begin() + i, index.begin() + i + 1);
				i--;
				break;
			}
		}
	}
	for (int i = 0; i < index.size(); i++)
	{
		cout << index[i].first;
	}
	for (int i = 0; i < index.size(); i++)
	{
		if (index[i].second == location)
		{
			answer = i + 1;
		}
	}
	cout << endl << answer;
	return answer;
}