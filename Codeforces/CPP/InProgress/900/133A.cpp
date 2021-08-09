#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    string input;
    cin >> input;
    string answer = "NO";
    for (int i = 0; i < input.length(); i++) {
        if (input[i] == 'H' || input[i] == 'Q' || input[i] == '9') {
            answer = "YES";
            break;
        }
    }
    cout << answer;
}