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
    int answer = 0;
    while(n != 0) {
        n--;
        answer++;
        if(answer % m == 0) {
            n++;
        }
    }
    cout << answer;
}