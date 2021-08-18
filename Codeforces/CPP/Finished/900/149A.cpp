#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int plant;
    cin >> plant;
    int months[12];
    for (int i = 0; i < 12; i++) {
        int month;
        cin >> month;
        months[i] = month;
    }
    sort(months, months + 12);
    int i = 11;
    int answer = 0;
    int counter = 0;
    while (i >= 0) {
        if (answer >= plant) {
            break;
        }
        else {
            answer += months[i];
            i -= 1;
            counter += 1;
        }
    }
    if(answer >= plant) {
        cout << counter;
    }
    else {
        cout << -1;
    }
}