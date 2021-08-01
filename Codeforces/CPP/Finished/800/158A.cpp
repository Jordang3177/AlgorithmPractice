#include <iostream>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int array[n];
    for(int i = 0; i < n; i++){
        int w;
        cin >> w;
        array[i] = w;
    }
    int specialNumber = array[k - 1];
    int answer = 0;
    // (&array + 1) refers to the memory address one place after the end of the array and adding * to the front assigns this number to an integer. 
    // then if you subtract that by the start address of the array you will get the length of the array.
    for(int j = 0; j < *(&array + 1) - array; j++){
        if (array[j] >= specialNumber && array[j] > 0){
            answer += 1;
        }
    }
    cout << answer << endl;
    return 0;
}