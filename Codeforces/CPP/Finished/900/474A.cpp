#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    string s = "qwertyuiopasdfghjkl;zxcvbnm,./";
    char shift; 
    string words;
    cin >> shift >> words;
    string answer;
    for(int i = 0; i < words.length(); i++) {
        char letter = s.find(words[i]);
        if (shift == 'R') {
            answer += s[letter - 1];
        }
        else {
            answer += s[letter + 1];
        }
    }
    cout << answer;
}