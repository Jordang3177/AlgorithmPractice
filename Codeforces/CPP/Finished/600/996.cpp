#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n;
    int answer = 0;
    cin >> n;
    while (n > 0)
    {
        if (n >= 100)
        {
            n -= 100;
            answer += 1;
        }
        else if (n >= 20)
        {
            n -= 20;
            answer += 1;
        }
        else if (n >= 10)
        {
            n -= 10;
            answer += 1;
        }
        else if (n >= 5)
        {
            n -= 5;
            answer += 1;
        }
        else
        {
            n -= 1;
            answer += 1;
        }
    }
    cout << answer << endl;
    return 0;
}