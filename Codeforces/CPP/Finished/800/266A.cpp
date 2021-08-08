#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string colors;
    cin >> colors;
    char previous = colors[0];
    int answer = 0; 
    for (int i = 1; i < n; i++)
    {
        if (previous == colors[i])
        {
            answer += 1;
        }
        previous = colors[i];
    }
    cout << answer;
    return 0;
}