#include <iostream>
#include <math.h>
using namespace std;


int main()
{
  int a;
  cin >> a;
  float sqrtn = sqrt(a);
  int sqrtn1 = sqrt(a);
  if(sqrtn - sqrtn1 == 0){
    cout << "Integer";
  }
  else{
    cout << "Float";
  }
	return 0;
}