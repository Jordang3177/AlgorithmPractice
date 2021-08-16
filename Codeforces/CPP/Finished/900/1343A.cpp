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
        int n;
        cin >> n;
        for (int j = 2; j < n; j++)
        {
            int val = pow(2, j) - 1;
            if (n % val == 0)
            {
                int x = n / val;
                cout << x << endl;
                break;
            }
        }
    }
}