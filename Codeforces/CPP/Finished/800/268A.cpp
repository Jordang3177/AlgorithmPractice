#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++) {
        int h, a;
        cin >> h >> a;
        pair<int, int> p(h, a);
        v.push_back(p);
    }
    int answer = 0;
    for (int i = 0; i < v.size(); i++) {
        for(int j = 0; j < v.size(); j++) {
            if(i == j) {
                continue;
            }
            int home = v[i].first;
            int away = v[j].second;
            if(home == away) {
                answer += 1;
            }
        }
    }
    cout << answer;
}