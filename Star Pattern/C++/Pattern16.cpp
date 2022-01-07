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
    for(int i =1;i<=n;i++){
        if (i == 1){
            for(int j = 0;j<=n;j++){
            cout << " ";
        }
        }
        else if (1 < i < n-1)
        {
            for(int j = 0;j<=n-i;j++){
                cout << " ";
            }
            cout << "*";
            for(int j = 1;j<=i-1;j++){
                cout << " ";
            }
        }
        cout << "*" << endl;
    }
    for(int i = 0; i<=n+1;i++){
        cout << "*";
    }
}