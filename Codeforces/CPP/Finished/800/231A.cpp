#include <iostream>

using namespace std;

int main()
{
    int n;
    int output = 0;
    cin >> n;
    for (int i = 0; i < n; i++){
        int one, two, three;
        cin >> one >> two >> three;
        int sum = one + two + three;
        if (sum >= 2){
            output += 1;
        }
    }
    cout << output << endl;
    return 0;
}