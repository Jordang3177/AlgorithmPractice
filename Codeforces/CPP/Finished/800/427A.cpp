#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int answer = 0;
    int holder = 0;
    for (int i = 0; i < n; i++) {
        int pc;
        cin >> pc;
        if(pc == -1) {
            if (holder == 0) {
                answer += 1;
            }
            else {
                holder -= 1;
            }
        }
        else {
            holder += pc;
        }
    }
    cout << answer;
}