#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    string s;
    cin >> s;
    string answer;
    for (int i = 0; i < s.length(); i++) {
        char lowered = tolower(s[i]);
        if (lowered == 'a' || lowered == 'e' || lowered == 'i' || lowered == 'o' || lowered == 'u' || lowered == 'y') {
            continue;
        }
        else {
            answer += '.';
            answer += lowered;
        }
    }
    cout << answer;
}