#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int answer = 0;
    for (int i = 1; i < (n / 2) + 1; i++)
    {
        int holder;
        holder = n - i;
        if (holder % i == 0)
        {
            answer += 1;
        }
    }
    cout << answer << endl;
    return 0;
}