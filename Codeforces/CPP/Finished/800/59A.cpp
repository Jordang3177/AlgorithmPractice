#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    string n;
    cin >> n;
    int upperCase = 0;
    int lowerCase = 0;
    for (int i = 0; i < n.length(); i++) {
        if (int(n[i]) > 90) {
            lowerCase += 1;
        }
        else {
            upperCase += 1;
        }
    }
    if (upperCase > lowerCase){ 
        for (int i = 0; i < n.length(); i++) {
            n[i] = toupper(n[i]);
        }
    }
    else {
        for (int i = 0; i < n.length(); i++) {
            n[i] = tolower(n[i]);
        }
    }
    cout << n;
}