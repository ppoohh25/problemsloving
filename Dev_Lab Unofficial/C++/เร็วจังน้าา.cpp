#include <iostream>
#include <iomanip>
using namespace std;


int main()
{
  float time;
  cin >> time;
	float v = 0.04/(time/3600);

  cout << fixed;
  cout << setprecision(2);
  cout << v << " km/hr";
	return 0;
}