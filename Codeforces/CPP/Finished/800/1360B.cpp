#include <bits/stdc++.h>

using namespace std;

#define endl "\n"

int main()
{
    int tests;
    cin >> tests;
    for(int i = 0; i < tests; i++) {
        int length;
        cin >> length;
        vector<int> athletes;
        for(int j = 0; j < length; j++) {
            int athlete;
            cin >> athlete;
            athletes.push_back(athlete);
        }
        sort(athletes.begin(), athletes.end());
        int minimum = INT_MAX;
        for(int j = 0; j < length - 1; j++) {
            int current = athletes.at(j);
            int next = athletes.at(j + 1);
            if((next - current) < minimum) {
                minimum = next - current;
            }
        }
        cout << minimum << '\n';
    }
    return 0;
}