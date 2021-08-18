#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int answer = 0;
    int tv_prices[n];
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        tv_prices[i] = a;
    }
    sort(tv_prices, tv_prices + n);
    for (int i = 0; i < m; i++ ) {
        if(tv_prices[i] < 0) {
            answer += tv_prices[i];
        }
        else {
            break;
        }
    }
    answer *= -1;
    cout << answer;
}