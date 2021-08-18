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
    string numbers;
    cin >> numbers;
    int zeroes = 0;
    int ones = 0;
    for (int i = 0; i < n; i++) {
        if (numbers[i] == '0') {
            zeroes++;
        }
        else {
            ones++;
        }
    }
    cout << abs(zeroes - ones);
}