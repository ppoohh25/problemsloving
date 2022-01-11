#include <iostream>
#include <math.h>
using namespace std;


int main()
{
  int a,b;
  cin >> a;
  cin >> b;
  int d = 1;
  for(int i = 0;i<b;i++){
    d *= a;
  }
  cout << d;
	return 0;
}