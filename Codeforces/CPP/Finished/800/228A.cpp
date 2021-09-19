#include <bits/stdc++.h>

using namespace std;

int main()
{
    int one, two, three, four;
    cin >> one >> two >> three >> four;
    int answer = 0;
    if (one == two || one == three || one == four) {
        answer += 1;
    }
    if (two == three || two == four) {
        answer += 1;
    }
    if (three == four) {
        answer += 1;
    }
    cout << answer;
}