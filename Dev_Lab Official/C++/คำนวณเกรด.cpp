#include <iostream>
using namespace std;


int main()
{
  int n;
  cin >> n;
  if(80 <= n && n <= 100){
    cout << "A";
  }
  else if(70 <= n && n <= 79){
    cout << "B";
  }
  else if(60 <= n && n <= 69){
    cout << "C";
  }
  else if(50 <= n && n <= 59){
    cout << "D";
  }
  else if(n < 50){
    cout << "F";
  }
	return 0;
}