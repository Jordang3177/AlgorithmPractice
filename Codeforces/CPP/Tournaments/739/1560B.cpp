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
    for (int i = 0; i < t; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        int k = abs(a - b) * 2;
        int diff = k / 2;
        if (a > k || b > k || c > k)
        {
            cout << -1 << endl;
        }
        else
        {
            int right = c + diff;
            int left = c - diff;
            if (left > 0)
            {
                cout << left << endl;
            }
            else if (right <= k)
            {
                cout << right << endl;
            }
            else
            {
                cout << -1 << endl;
            }
        }
    }
}