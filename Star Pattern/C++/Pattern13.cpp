/*
*****
 ****
  ***
   **
    *
   **
  ***
 ****
*****
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n;i++){
        for(int j = 0; j < i;j++){
            cout << " ";
        }
        for(int k = 1; k <= n-i;k++){
            cout << "*";
        }
        cout << "\n";
    }
    for(int i = 2;i<=n;i++){
        for(int j = 1;j<=n-i;j++){
            cout << " ";
        };
        for(int k = 1;k<=i;k++){
            cout << "*";
        };
        cout << "\n";
    };
}