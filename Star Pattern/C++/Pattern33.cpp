/*
* * *
*   *
*   *
*   *
 ***
*   *
*   *
*   *
* * *
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n-1;i++){
        if(i == 0){
            cout << "* * *";
        }
        else{
            cout << "*   *";
        }
        cout << endl;
    }
    cout << " ***" << endl;
    for(int i = 0;i<n-1;i++){
        if(i == n-2){
            cout << "* * *";
        }
        else{
            cout << "*   *";
        }
        cout << endl;
    }
}