#include <iostream>
using namespace std;


int main()
{
  int n = 5;
  for(int i =0;i<n;i++){
    for(int j =0;j<n-1-i;j++){
      cout << " ";
    }
    if(i == 0){
      cout << "$";
    }
    else{
      for(int j = 0;j < i;j++){
        cout << "$ ";
      }
      cout << "$";
    }
    cout << endl;
  }
	return 0;
}