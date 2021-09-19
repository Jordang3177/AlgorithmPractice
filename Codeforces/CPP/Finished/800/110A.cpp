#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long n;
    cin >> n;
    int lucky = 0;
    int current;
    while(n != 0) {
        current = n % 10;
        if (current == 4 || current == 7){
            lucky += 1;
            n /= 10;
        }
        else {
            n /= 10;
        }
    }
    if (lucky == 4 || lucky == 7) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}