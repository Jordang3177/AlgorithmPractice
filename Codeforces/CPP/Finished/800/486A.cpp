#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    cin >> n;
    if (n % 2 != 0) {
        n /= 2;
        n++;
        n *= -1;
    }
    else {
        n /= 2;
    }
    cout << n;
}