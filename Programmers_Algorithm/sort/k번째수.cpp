#include <string>
#include <vector>
#include<iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer, array1;
	int temp;
	for (int i = 0; i< commands.size(); i++)
	{
		array1 = array;
		for (int j = commands[i][0] - 1; j < commands[i][1]; j++)
		{
			for (int k = commands[i][0] - 1; k < commands[i][1]; k++)
			{
				if (array1[j] < array1[k])
				{
					temp = array1[j];
					array1[j] = array1[k];
					array1[k] = temp;

				}
			}
		}
		answer.push_back(array1[commands[i][2] + commands[i][0] - 2]);
	}
	return answer;
}