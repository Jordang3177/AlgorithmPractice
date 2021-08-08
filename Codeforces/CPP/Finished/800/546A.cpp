#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int initialB, dollars, wantB;
    cin >> initialB >> dollars >> wantB;
    int nextB = 1;
    int answer = 0;
    for (int i = 0; i < wantB; i++){
        answer += nextB * initialB;
        nextB += 1;
    }
    answer -= dollars;
    if (answer < 0){
        cout << 0;
        return 0;
    }
    cout << answer;
    return 0;
}