#include <iostream>
#include <cmath>
using namespace std;


int main()
{
	float n;
  cin >> n;
  float a = pow(n,0.5);
  int b = pow(n,0.5);
  if(a == b){
    cout << a;
  }
  else{
    cout << "No Numbers Matching!";
  }
	return 0;
}