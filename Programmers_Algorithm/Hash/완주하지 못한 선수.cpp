#include <string>
#include <vector>
#include<map>
#include<iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";
	map <string, int> x, y;
	for (int i = 0; i < participant.size(); i++)
	{
		x[participant[i]]++;
	}
	for (int i = 0; i < completion.size(); i++)
	{
		x[completion[i]]--;
	}
	for (int i = 0; i < participant.size(); i++)
	{
		if (x[participant[i]] > 0)
		{
			//cout << participant[i]<<endl;
			answer = participant[i];
		}
	}

	return answer;
}