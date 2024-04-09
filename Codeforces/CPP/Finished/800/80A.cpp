#include <bits/stdc++.h>

using namespace std;

#define endl "\n"

int main()
{
    int a, b;
    cin >> a >> b;
    bool isPrime = true;
    for(int i = 2; i < b; i++) {
        if(b % i == 0) {
            isPrime = false;
            break;
        }
    }
    if(!isPrime) {
        cout << "NO";
        return 0;
    }
    bool isNextPrime = true;
    for(int i = a + 1; i < b; i++) {
        isPrime = true;
        for(int j = 2; j < i; j++) {
            if(i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime) {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
    return 0;
}