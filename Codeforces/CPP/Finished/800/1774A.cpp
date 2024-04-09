#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int length;
        cin >> length;
        string a;
        cin >> a;
        int sum;
        if(a[0] == '0') {
            sum = 0;
        }
        else {
            sum = 1;
        }
        string answer = "";
        for(int j = 1; j < a.length(); j++) {
            if(a[j] == '0') {
                answer.append("+");
            }
            else if(sum > 0) {
                answer.append("-");
                sum -= 1;
            }
            else {
                answer.append("+");
                sum += 1;
            }
        }
        cout << answer << '\n';
    }
    return 0;
}