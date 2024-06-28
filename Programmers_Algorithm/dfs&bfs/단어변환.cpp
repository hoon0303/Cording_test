#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int rst = 100000;
bool word1(string begin, string word)
{
    int cnt=0;
    if(begin.size()!=word.size())
        return false;
    for(int i=0;i<begin.size();i++)
    {
        if(begin[i]!=word[i])
        {
            if(cnt==1)
                return false;
            cnt++;
        }
    }
    return true;
}
void dfs(int index, string target, vector<string> words, bool visited[],int cnt)
{
    if(words[index]==target)
    {
        rst = min(rst, cnt);
        return;
    }
    if(visited[index])
        return;
    visited[index]=true;
    for(int i=0;i<words.size();i++)
    {
        if(word1(words[index], words[i]))
        {
            dfs(i, target, words, visited, cnt+1);
        }
    }
    
}
int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    
    for(int i=0;i<words.size();i++)
    {
        if(word1(begin,words[i]))
        {
            bool visited[51] = {0};
            dfs(i,target, words,visited, 1);
        }
    }
    if(rst == 100000)
        rst = 0;
    return rst;
}