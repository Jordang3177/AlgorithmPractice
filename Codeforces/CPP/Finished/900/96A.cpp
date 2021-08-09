#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    string players;
    cin >> players;
    int zeroes = 0, ones = 0;
    string answer = "NO";
    for (int i = 0; i < players.length(); i++){
        if (players[i] == '0') {
            zeroes += 1;
            ones = 0;
        }
        else {
            ones += 1;
            zeroes = 0;
        }
        if (zeroes >= 7 || ones >= 7) {
            answer = "YES";
            break;
        }
    }
    cout << answer;
}