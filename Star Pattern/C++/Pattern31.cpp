/*
*   *
 * *
  *
 * *
*   *
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n/2;i++){
        for(int j =0;j<i;j++){
            cout << " ";
        }
        cout << "*";
        for(int j =0;j<((n-3)*2+1)-(i-1)*2-n+1;j++){
            cout << " ";
        }
        cout << "*" << endl;
    }
    for(int i =0;i<n/2;i++){
        cout << " ";
    }
    cout << "*" << endl;
    for(int i = 0;i<n/2;i++){
        for(int j = 0;j<=n/2-2-i;j++){
            cout << " ";
        }
        cout << "*";
        for(int j = 0;j<i*2+1;j++){
            cout << " ";
        }
        cout << "*" << endl;
    }
}