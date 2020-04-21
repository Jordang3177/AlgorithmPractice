#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int participants, pens, notebooks;
    cin >> participants >> pens >> notebooks;
    if (pens >= participants && notebooks >= participants)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}