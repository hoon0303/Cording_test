#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main(void)
{
	int T;
	scanf("%d", &T);

	int x1, y1, x2, y2, r1, r2;
	double len;
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

		if (x1 == x2&&y1 == y2)//원의 중심이 같은 경우
		{
			if (r1 == r2)//두원이 중첨되기 때문에 교점 무제한
			{
				printf("-1\n");
				continue;
			}
			else
			{
				printf("0\n");
				continue;
			}
		}
		len = sqrt(pow((x1 - x2), 2) + pow(y1 - y2, 2));//원의 중점사이의 거리

		if (len == r1 + r2 || len + r1 == r2 || len + r2 == r1)//교점이 한개인 경우
		{
			printf("1\n");
			continue;
		}
		if (len > r1 + r2 || len + r1 < r2 || len + r2 < r1)
		{
			printf("0\n");
			continue;
		}
		printf("2\n");
	}
	return 0;
}