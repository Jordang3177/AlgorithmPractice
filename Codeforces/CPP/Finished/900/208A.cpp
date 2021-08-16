#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int main()
{
    string song;
    cin >> song;
    string answer;
    bool space_needed = false;
    int i = 0;
    while (i < song.length()) {
        if (song[i] == 'W' && song[i + 1] == 'U' && song[i + 2] == 'B') {
            if(space_needed){
                answer += ' ';
            }
            i += 3;
        }
        else{
            answer += song[i];
            space_needed = true;
            i += 1;
        }
    }
    cout << answer;
}