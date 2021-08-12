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
    int boxes[n];
    for (int i = 0; i < n; i++){
        int box;
        cin >> box;
        boxes[i] = box;
    }
    sort(boxes, boxes + n);
    for (int i = 0; i < n; i++){
        cout << boxes[i] << " ";
    }
}