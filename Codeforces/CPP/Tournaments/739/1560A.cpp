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
        int k;
        cin >> k;
        int j = 1;
        int counter = 0;
        while (j != k + 1) {
            counter += 1;
            if(counter >= 3) {
                if(counter % 3 == 0 || (counter - 3) % 10 == 0) {
                    continue;
                }
                else {
                    j += 1;
                }
            }
            else {
                j += 1;
            }
        }
        cout << counter << endl;
    }
}