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
    if(n >= 0){
        cout << n;
    }
    else if (n >= -10) {
        cout << 0;
    }
    else {
        string left = to_string(n);
        string right = to_string(n);
        char left_end = left[left.size() - 1];
        left = left.erase(left.size() - 2);
        left += left_end;
        right = right.erase(right.size() - 1);
        int n_left = stoi(left);
        int n_right = stoi(right);
        if(n_left < n_right) {
            cout << n_right;
        }
        else {
            cout << n_left;
        }
    }
}