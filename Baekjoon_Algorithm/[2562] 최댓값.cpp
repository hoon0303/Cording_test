#include<iostream>
using namespace std;
int main(void)
{
    int x;
    int max=0,index=0;
    for(int i=0;i<9;i++)
    {
        int temp;
        cin>>temp;
        if(max<temp)
        {
            max=temp;
            index=i+1;
        }
    }
    cout<<max<<endl<<index;
}