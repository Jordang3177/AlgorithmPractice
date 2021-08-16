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
        for(int j = 0; j < n; j++){
            int a;
            cin >> a;
            arr[j] = a;
        }
        sort(arr, arr + n);
        cout << (arr[0] & arr[n - 1]) << endl;
    }
}