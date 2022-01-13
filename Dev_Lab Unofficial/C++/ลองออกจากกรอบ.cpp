#include <iostream>
using namespace std;


int main()
{
	int n;
  cin >> n;
  if(n<=2){
    cout << "Box's height must be more than 2";
  }
  else{
  for(int i = 0;i<n;i++){
    if(i == 0 || i == n-1){
      for(int j = 0;j<n;j++){
        cout << "#";
      }
    }
    else{
      cout << "#";
      for(int j = 0;j<n-2;j++){
        cout << " ";
      }
      cout << "#";
    }
    cout << endl;
  }
  }
	return 0;
}