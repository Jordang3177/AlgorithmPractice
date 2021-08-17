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
        int n;
        cin >> n;
        int count2 = 0;
        int count3 = 0;
        while(n % 2 == 0) {
            n /= 2;
            count2++;
        }
        while(n % 3 == 0) {
            n /= 3;
            count3++;
        }
        if (n == 1 && count3 >= count2) {
            cout << (count3 - count2) + count3 << endl;
        }
        else {
            cout << -1 << endl;
        }
    }
}