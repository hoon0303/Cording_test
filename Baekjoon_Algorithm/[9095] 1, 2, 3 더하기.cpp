#include<stdio.h>
int main(void)
{
	int i,x,j;
	int sum=0;
	int test_case;
	int dp[3]={1,2,4};
	 scanf("%d",&test_case);
	for(i=0;i<test_case;i++)
	{
		sum=0;
		dp[0]=1;
		dp[1]=2;
		dp[2]=4;
		scanf("%d",&x);
		if(x<=3)
			sum=dp[x-1];
		else
		{
		for(j=3;j<x;j++)
		{
			sum=dp[0]+dp[1]+dp[2];
			dp[0]=dp[1];
			dp[1]=dp[2];
			dp[2]=sum;
		}
		}
		printf("%d\n",sum);
	}
}
