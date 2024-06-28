#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
 
int answer = 9;
 
void dfs(int N, int number, int count, int currentNumber) {
    //일정횟수 이상갔다면 리턴
    if (count >= 9)        return;
    //현재수가 number와 같다면 작은횟수를 answer에 저장후 리턴
    if (currentNumber == number) {
        answer = min(answer, count);
        return;
    }
    int tempNumber = 0;
    //최대 N의 사용횟수는 9번까지이므로 이때까지 반복
    for (int i = 0; i + count< 9 ; i++) {
        //N부터 NN,NNN,NNNN .....
        tempNumber = tempNumber * 10 + N;
        //더하기 빼기 곱하기 나누기 dfs 사용
        dfs(N, number, count + 1 + i, currentNumber + tempNumber);
        dfs(N, number, count + 1 + i, currentNumber - tempNumber);
        dfs(N, number, count + 1 + i, currentNumber * tempNumber);
        dfs(N, number, count + 1 + i, currentNumber / tempNumber);
    }
}
 
int solution(int N, int number) {
    dfs(N, number, 0, 0);
    //answer가 9라는 뜻은 number와 맞는 경우가 없었던 것이므로 -1 리턴
    if (answer == 9)    return -1;
    return answer;
}