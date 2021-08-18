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
    for (int i = 0; i < t; i++) {
        int hp, voidA, lightS;
        cin >> hp >> voidA >> lightS;
        while(voidA) {
            if(hp < 20){
                break;
            }
            hp = (hp / 2) + 10;
            voidA -= 1;
        }
        while(lightS){
            hp -= 10;
            lightS -= 1;
        }
        if (hp <= 0) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}