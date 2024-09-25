#include<stdio.h>
#include<math.h>
int main()
{
	int a, b,rst=1;
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		rst = 1;
		scanf("%d %d", &a, &b);
		for (int j = 0; j < b; j++)
		{
			rst = rst*a % 10;
		}

		if (rst == 0)
			rst = 10;
		printf("%d\n", rst);
		
	}
	return 0;
}
