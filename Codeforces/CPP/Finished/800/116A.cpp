#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int max_answer = 0;
    int answer = 0;
    for (int i = 0; i < n; i++) {
        int out, in;
        cin >> out >> in;
        answer -= out;
        answer += in;
        max_answer = max(max_answer, answer);
    }
    cout << max_answer;
}