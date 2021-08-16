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
    if (min(n, m) % 2 == 1) {
        cout << "Akshat";
    }
    else {
        cout << "Malvika";
    }
}