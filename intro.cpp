#include <iostream>
#include <string>
#include <vector>
#
using namespace std;

int count(int arr[]) {
    for (int i  = 0; i < sizeof(arr) / sizeof(arr[0]); ++i) {
        cout << arr[i];
    }
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7};
    cout << "Hello, World!" << std::endl;
    count(arr);
    return 0;
}

