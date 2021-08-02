#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    string inputWord;
    cin >> inputWord;
    inputWord[0] = (char) toupper(inputWord[0]);
    cout << inputWord;
    return 0;
}