#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main()
{
    string characters;
    cin >> characters;
    set<char> s1;
    for (int i = 0; i < characters.length(); i++)
    {
        s1.insert(characters[i]);
    }
    if(s1.size() % 2 == 0)
    {
        cout << "CHAT WITH HER!";
        return 0;
    }
    else
    {
        cout << "IGNORE HIM!";
        return 0;
    }
}