#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int answer = 0;
    for(int i = 0; i < n; i ++){
        string operation;
        cin >> operation;
        if(operation[0] == '+' || operation[1] == '+'){
            answer += 1;
        }
        else {
            answer -= 1;
        }
    }
    cout << answer;
    return 0;
}