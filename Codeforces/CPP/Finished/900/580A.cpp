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
    int count = 0;
    int past = 0;
    int max_length = 0;
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        if (k >= past) {
            count += 1;
            past = k;
        }
        else {
            max_length = max(max_length, count);
            count = 1;
            past = k;
        }
    }
    max_length = max(max_length, count);
    cout << max_length;
}