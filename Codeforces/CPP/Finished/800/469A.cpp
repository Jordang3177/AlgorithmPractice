#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    set<int> answer;
    int p;
    cin >> p;
    for (int i = 0; i < p; i++) {
        int p_i;
        cin >> p_i;
        answer.insert(p_i);
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int q_i;
        cin >> q_i;
        answer.insert(q_i);
    }
    if(answer.size() == n) {
        cout << "I become the guy.";
    }
    else {
        cout << "Oh, my keyboard!";
    }
}