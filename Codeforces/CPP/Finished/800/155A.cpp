#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int answer = 0;
    int min;
    cin >> min;
    int max = min;
    for (int i = 1; i < n; i++) {
        int holder;
        cin >> holder;
        if(holder > max) {
            answer++;
            max = holder;
        }
        if(holder < min) {
            answer++;
            min = holder;
        }
    }
    cout << answer;
}