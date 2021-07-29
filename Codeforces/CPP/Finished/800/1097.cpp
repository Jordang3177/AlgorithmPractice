#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    vector<string> v(5);
    string table;
    cin >> table;
    for (int i = 0; i < 5; i++)
    {
        cin >> v[i];
    }
    bool found = false;
    for (int i = 0; i < v.size(); i++)
    {
        if (table[0] == v[i][0] || table[1] == v[i][1])
        {
            found = true;
        }
    }
    if (found)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
}