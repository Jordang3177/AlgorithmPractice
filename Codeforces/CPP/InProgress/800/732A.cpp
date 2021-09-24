#include <bits/stdc++.h>

using namespace std;

int main()
{
    int k, r;
    cin >> k >> r;
    int answer = 1;
    int holder = k;
    while(k % 10 != 0 && k % 10 != r && answer != 10) {
        k += holder;
        answer += 1;
    }
    cout << answer;
}