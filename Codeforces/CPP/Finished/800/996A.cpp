#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int answer = 0;
    if (n >= 100) {
        answer += n / 100;
        n %= 100;
    }
    if (n >= 20) {
        answer += n / 20;
        n %= 20;
    }
    if (n >= 10) {
        answer += n / 10;
        n %= 10;
    }
    if (n >= 5) {
        answer += n / 5;
        n %= 5;
    }
    answer += n;
    cout << answer;
    return 0;
}