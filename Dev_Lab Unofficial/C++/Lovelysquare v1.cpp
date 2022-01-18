#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


int main()
{
	double d;
  cin >> d;
  double area = 0.5*d*d;
  double l = pow(pow(d/2,2)*2,0.5);
  cout << fixed << setprecision(2) << l*4 << endl;
  cout << fixed << setprecision(2) << area;
	return 0;
}