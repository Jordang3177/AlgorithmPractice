#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    string a, b;
    cin >> a;
    cin >> b;
    int answerA = 0, answerB = 0;
    for(int i = 0; i < a.length(); i++)
    {
        answerA += tolower(a[i]);
        answerB += tolower(b[i]);
        if (answerA > answerB)
        {
            cout << 1 << endl;
            return 0;
        }
        if (answerB > answerA)
        {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << 0;
    return 0;
}