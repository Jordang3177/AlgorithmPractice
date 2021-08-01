#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int specialNumber;
    int x, y;
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            cin >> specialNumber;
            if (specialNumber == 1){
                x = i + 1;
                y = j + 1;
            }
        }
    }
    int answerx = 0, answery = 0;
    answerx = abs(x - 3);
    answery = abs(y - 3);
    int answer = answerx + answery;
    cout << answer;
    return 0;
}