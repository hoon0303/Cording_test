#include<iostream>

using namespace std;

int main(void)
{
	int x = 1, y = 1;
	while (1)
	{
		cin >> x >> y;
		if (x == 0 && y == 0)
			break;
		cout << x + y << endl;
	}
}
