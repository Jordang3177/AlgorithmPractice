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
    while (n > 0){
        if (n >= 5){
            n -= 5;
            answer += 1;
        }
        else if (n == 4){
            n -= 4;
            answer += 1;
        }
        else if (n == 3) {
            n -= 3;
            answer += 1;
        }
        else if (n == 2) {
            n -= 2;
            answer += 1;
        }
        else if (n == 1) {
            n -= 1;
            answer += 1;
        }
    }
    cout << answer;
}