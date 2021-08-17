#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, a, b;
        int x = 'a';
        int cnt = 0;
        cin >> n >> a >> b;
        for (int j = 0; j < n; j++) {
            cout << char(x + cnt);
            cnt++;
            if (cnt > b - 1) {
                cnt = 0;
            }
        }
        cout << endl;
    }
}