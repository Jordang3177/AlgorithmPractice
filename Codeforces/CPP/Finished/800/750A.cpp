#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int answer = 0;
    if (k >= 240) {
        cout << answer;
        return 0;
    }
    else {
        int constant = 5;
        for(int i = 0; i < n; i++) {
            k += constant;
            if(k > 240) {
                cout << answer;
                return 0;
            }
            constant += 5;
            answer++;
        }
        cout << answer;
    }
}