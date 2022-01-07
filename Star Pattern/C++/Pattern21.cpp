/*
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for(int i =0;i<n;i++){
        if(i == 0){
            for(int j = 0;j<n-1;j++){
                cout << " ";
            }
            cout << "*";
        }
        else{
            for(int j = 0;j<n-1-i;j++){
                cout << " ";
            }
            cout << "*";
            for(int j = 0;j<2*i-1;j++){
                cout << " ";
            }
            cout << "*";
        }
        cout << endl;
    }
    for(int i = 1;i<n;i++){
        if (i == n-1)
        {
            for(int j = 0;j<n-1;j++){
                cout << " ";
            }
            cout << "*";
        }
        else{
            for(int j =0;j<i;j++){
                cout << " ";
            }
            cout << "*";
            for(int j =0;j<((n-3)*2+1)-(i-1)*2;j++){
                cout << " ";
            }
            cout << "*";
        }
        cout << endl;
        
    }
}