#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<string, int> vals;
    vals["T"] = 4;
    vals["C"] = 6;
    vals["O"] = 8;
    vals["D"] = 12;
    vals["I"] = 20;
    int n;
    cin >> n;
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        s = s.at(0);
        res += vals[s];
    }
    cout << res << endl;
    return 0;
}