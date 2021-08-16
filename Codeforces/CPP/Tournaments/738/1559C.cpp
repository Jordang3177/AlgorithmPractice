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
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        int arr[n];
        for (int j = 0; j < n; j++){
            int a;
            cin >> a;
            arr[j] = a;
        }
        for (int j = 0; j < n + 1; j++) {
            if (j != n){
                cout << j + 1 << ' ';
            }
            else {
                cout << j + 1 << endl;
            }
        }
    }
}