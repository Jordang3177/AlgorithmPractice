#include <bits/stdc++.h>

using namespace std;

int main() {
    int s, n;
    cin >> s >> n;
    vector<pair<int, int>> dragons;
    for (int i = 0; i < n; i++) {
        int dragon, bonus;
        cin >> dragon >> bonus;
        dragons.push_back(make_pair(dragon, bonus));
    }
    sort(dragons.begin(), dragons.end());
    for(int i = 0; i < n; i++) {
        if(dragons[i].first >= s){
            cout << "NO";
            return 0;
        }
        s += dragons[i].second;
    }
    cout << "YES";
    return 0;
}