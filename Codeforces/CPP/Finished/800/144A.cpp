#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int a[n];
    pair<int, int> maximum;
    maximum.first = -1;
    pair<int, int> minimum;
    minimum.first = 101;
    for (int i = 0; i < n; i++) {
        int ai;
        cin >> ai;
        if(maximum.first < ai) {
            maximum.first = ai;
            maximum.second = i;
        }
        if(minimum.first >= ai) {
            minimum.first = ai;
            minimum.second = i;
        }
        a[i] = ai;
    }
    int answer = 0;
    answer = abs((n - 1) - minimum.second);
    answer += maximum.second;
    if(maximum.second > minimum.second) {
        answer -= 1;
    }
    cout << answer;
    return 0;
}