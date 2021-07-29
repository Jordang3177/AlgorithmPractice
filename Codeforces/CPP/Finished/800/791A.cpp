#include <iostream>

using namespace std;

int main()
{
    int small, big;
    cin >> small >> big;
    int answer = 0;
    while (small <= big)
    {
        answer += 1;
        small *= 3;
        big *= 2;
    }
    cout << answer << endl;

    return 0;
}