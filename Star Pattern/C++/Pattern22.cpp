/*
*
* *
*  *
*   *
*    *
*   *
*  *
* *
*
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n; i++){
        cout << "*";
        for(int j = 0;j<i;j++){
            cout << " ";
        }
        if(i > 0){
            cout << "*";
        }
        
        cout << endl;
    }
    for(int i = 0;i<n-1;i++){
        if(i == n-2){
            cout << "*";
        }
        else{
            cout << "*";
            for(int j = 0;j<(n-2)-i;j++){
                cout << " ";
            }
            cout << "*";
        }

        cout << endl;
    }
}