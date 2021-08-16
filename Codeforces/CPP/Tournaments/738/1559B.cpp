#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        if (n == 0)
        {
            cout << endl;
        }
        if (n == 1 && s[0] == '?')
        {
            cout << 'B' << endl;
        }
        else if (n == 1 && s[0] != '?')
        {
            cout << s << endl;
        }
        else
        {
            char first;
            int position;
            bool found = false;
            int counter = 0;
            for (int j = 0; j < n; j++)
            {
                if (s[j] != '?')
                {
                    first = s[j];
                    position = j;
                    found = true;
                    break;
                }
                else
                {
                    counter += 1;
                }
            }
            if (!found && counter != n)
            {
                cout << s << endl;
            }
            else if (counter == n)
            {
                s[0] = 'B';
                char previous = 'B';
                for (int m = 1; m < n; m++)
                {
                    if (previous == 'B') {
                        s[m] = 'R';
                        previous = 'R';
                    }
                    else {
                        s[m] = 'B';
                        previous = 'B';
                    }
                }
                cout << s << endl;
            }
            else
            {
                char previous = first;
                for (int k = position - 1; k >= 0; k--)
                {
                    if (s[k] == '?')
                    {
                        if (previous == 'B')
                        {
                            s[k] = 'R';
                            previous = 'R';
                        }
                        else if (previous == 'R')
                        {
                            s[k] = 'B';
                            previous = 'B';
                        }
                    }
                    else
                    {
                        previous = s[k];
                    }
                }
                previous = first;
                for (int l = position + 1; l < n; l++)
                {
                    if (s[l] == '?')
                    {
                        if (previous == 'B')
                        {
                            s[l] = 'R';
                            previous = 'R';
                        }
                        else if (previous == 'R')
                        {
                            s[l] = 'B';
                            previous = 'B';
                        }
                    }
                    else
                    {
                        previous = s[l];
                    }
                }
                cout << s << endl;
            }
        }
    }
}