#include <string>
#include <vector>

using namespace std;
bool visited[201];
bool dfs(int i, vector<vector<int>> computers)
{
    if(visited[i])
    {
        return false;
    }
    visited[i]=true;
    
    for(int j=0;j<computers[i].size();j++)
    {
        if(computers[i][j]==1)
        {
            dfs(j,computers);
        }
    }
    return true;
    
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i=0;i<n;i++)
    {
        answer = answer + dfs(i, computers);
    }
    return answer;
}