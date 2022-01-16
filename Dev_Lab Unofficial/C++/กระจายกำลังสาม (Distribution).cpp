#include <iostream>
using namespace std;


int main()
{
	int a,b,c,d,e,f;
  cin >> a >> b >> c >> d >> e >> f;
  int A,B,C,D;
  A = a*c*e;
  B = (a*c*f) + (a*d*e) + (b*c*e);
  C = (a*d*f) + (b*c*f) + (b*d*e);
  D = b*d*f;
  cout << A << " " << B << " " << C << " " << D << " ";
	return 0;
}