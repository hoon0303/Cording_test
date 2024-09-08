//90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
#include<iostream>

using namespace std;

int main(void)
{
    int temp;
    cin>>temp;
    if(90<=temp)
        cout<<"A";
    else if(80<=temp)
        cout<<"B";
    else if(70<=temp)
        cout<<"C";
    else if(60<=temp)
        cout<<"D";
    else
        cout<<"F";
}
