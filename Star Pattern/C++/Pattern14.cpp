/*
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
*/
#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int k = n;
    for(int i = 1;i<=n;i++){
        for(int j =n;j>=1;j--){
            if (j <=k){
                cout << "* ";
            }else{
                cout << " ";
            }
        }
        k--;
        cout << endl;
    }
    int l = n-1;
    for(int i =2;i<=n;i++){
        for(int j =1;j<=n;j++){
            if (j >=l){
                cout << "* ";
            }else{
                cout << " ";
            }
        }
        l--;
        cout << endl;
    }
}