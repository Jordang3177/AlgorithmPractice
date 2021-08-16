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
    int arr[m];
    for(int i = 0; i < m; i++) {
        int puzzle;
        cin >> puzzle;
        arr[i] = puzzle;
    }
    int i = 0;
    sort(arr, arr + m);
    int answer = arr[m - 1];
    while (i < m - n + 1){
        answer = min(answer, arr[i + n - 1] - arr[i]);
        i++;
    }
    cout << answer;
}