#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int coins[n];
    for (int i = 0; i < n; i++) {
        int coin;
        cin >> coin;
        coins[i] = coin;
    }
    sort(coins, coins + n, greater<int>());
    int sum = 0;
    sum = accumulate(coins, coins + n, sum);
    int myCoins = 0;
    int half = sum / 2;
    int i = 0;
    int answer = 0;
    while (myCoins <= half){
        myCoins += coins[i];
        answer += 1;
        i += 1;
    }
    cout << answer;
}