#include <string>
#include <vector>
#include<queue>
#include<iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	int index = 0;
	int sum = 0;
	queue<int> q, len;
	while (1) {
		if (index < truck_weights.size())
		{
			if (weight >= sum + truck_weights[index])
			{
				sum = sum + truck_weights[index];
				q.push(truck_weights[index]);
				len.push(0);
				index++;
				//cout << "sum = " << sum << endl;
			}
		}
		if (q.empty())
			break;
		for (int i = 0; i < q.size(); i++)
		{
			int len1 = len.front() + 1;
			//cout << len1;
			len.pop();
			len.push(len1);
		}

		if (len.front() > bridge_length - 1 && !(len.empty()))
		{
			sum = sum - q.front();
			q.pop();
			len.pop();
		}
		answer++;

	}
	return answer + 1;
}