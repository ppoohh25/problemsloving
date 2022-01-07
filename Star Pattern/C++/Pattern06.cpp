/*
*********
 *******
  *****
   ***
    *
*/

#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<i;j++){
            cout << " ";
        }
        for(int k = 1;k<(2*n-(2*i));k++){
            cout << "*";
        }
        cout << endl;
    }
}