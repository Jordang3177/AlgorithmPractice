#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> a;
        for(int j = 0; j < n; j++) {
            int ai;
            cin >> ai;
            a.push_back(ai);
        }
        sort(a.begin(), a.end());
        int j = 0;
        while(j < a.size() - 1){
            if(abs(a[j] - a[j + 1]) <= 1) {
                vector<int>::iterator it;
                it = a.begin() + j;
                a.erase(it);
            }
            else {
                j++;
            }
        }
        if(a.size() == 1) {
            cout << "YES" << '\n';
        }
        else {
            cout << "NO" << '\n';
        }
    }
}