#include <iostream>
using namespace std;


int main()
{
  int a;
  int b;
  cin >> a;
  cin >> b;
  if(a > b){
    cout << "A";
  }
  else if(b > a){
    cout << "B";
  }
  else{
    cout << "AB";
  }
	return 0;
}