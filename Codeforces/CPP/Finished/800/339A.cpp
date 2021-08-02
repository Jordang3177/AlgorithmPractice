#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    string calculation;
    cin >> calculation;
    int counter = 0;
    for (int i = 0; i < calculation.length(); i++)
    {
        if (calculation[i] != '+')
        {
            counter += 1;
        }
    }
    int arrayOfNumbers[counter];
    counter = 0;
    for (int i = 0; i < calculation.length(); i++)
    {
        if (calculation[i] != '+'){
            arrayOfNumbers[counter] = (int) calculation[i];
            counter += 1;
        }
    }
    sort(arrayOfNumbers, arrayOfNumbers + counter);
    for (int i = 0; i < counter - 1; i++)
    {
        cout << (char) arrayOfNumbers[i] << '+';
    }
    cout << (char) arrayOfNumbers[counter - 1] << endl;
    return 0;
}