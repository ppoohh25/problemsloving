#include <iostream>
using namespace std;


int main()
{
	int n;
  cin >> n;
  if(n == 0){
    cout << "__";
  }
  else{
    for(int i = 0;i<n+1;i++){
      if(i == 0){
        for(int j = 0;j<n*3;j++){
          cout << " ";
        }
        cout << "__";
      }
      else{
        for(int j = 0;j<(n-i)*3;j++){
          cout << " ";
        }
        cout << "__|";
      }
      cout << endl;
    }
  }
	return 0;
}