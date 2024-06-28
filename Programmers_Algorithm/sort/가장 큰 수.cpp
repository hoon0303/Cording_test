#include <string>
#include <vector>
#include <algorithm>
#include<iostream>

using namespace std;

bool fun(string x, string y)
{
    if(stoi(x+y) > stoi(y+x))
        return true;
    return false;
}
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> arr;
    int check =0;
    for(int i=0;i<numbers.size();i++)
    {
        if(numbers[i]==0)
            check++;
        arr.push_back(to_string(numbers[i]));
    }
    //cout<<check;
    if(check==numbers.size())
        return "0";
    sort(arr.begin(), arr.end(),fun);
    for(int i=0;i<arr.size();i++)
    {
        //cout<<arr[i]<<" ";
        answer=answer+arr[i];
        
    }
    
    return answer;
}