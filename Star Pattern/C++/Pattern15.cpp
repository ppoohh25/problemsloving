/*
*
* *
*  *
*   *
******
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n-1; i++){
        cout << "*";
        for(int j = 0;j<i;j++){
            cout << " ";
        }
        if(i > 0){
            cout << "*";
        }
        
        cout << endl;
    }
    for(int i = 0; i < n+1;i++){
        cout << "*";
    }
}