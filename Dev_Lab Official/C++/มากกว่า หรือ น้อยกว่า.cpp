#include <iostream>
using namespace std;


int main()
{
  int a,b;
  cin >> a;
  cin >> b;
  if(a>b){
    cout << "MAX : " << a << endl;
    cout << "MIN : " << b << endl;
  }
  else{
    cout << "MAX : " << b << endl;
    cout << "MIN : " << a << endl;
  }
	return 0;
}