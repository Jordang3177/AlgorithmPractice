#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int people, time;
    cin >> people >> time;
    string line;
    cin >> line;
    for(int i = 0; i < time; i++) {
        int n = 0;
        while (n < line.length() - 1){
            if(line[n] == 'B' && line[n + 1] == 'G'){
                line[n] = 'G';
                line[n + 1] = 'B';
                n += 2;
            }
            else {
                n += 1;
            }
        }
    }
    cout << line;
}