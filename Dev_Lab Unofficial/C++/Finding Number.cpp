#include <iostream>
using namespace std;


int main()
{
  int n;
  cin >> n;
  int a[n];
  for(int i = 0;i<n;i++){
    cin >> a[i];
  }

  int b;
  int count;
  cin >> b;
  for(int i = 0;i<n;i++){
    if(b == a[i]){
      count = 1;
      break;
    }
  }
  if(count == 1){
    cout << "Yes";
  }
  else{
    cout << "No";
  }
	return 0;
}