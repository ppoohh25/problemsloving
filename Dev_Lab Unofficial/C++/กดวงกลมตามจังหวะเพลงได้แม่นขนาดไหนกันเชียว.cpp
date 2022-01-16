#include <iostream>
#include <iomanip>
using namespace std;


int main()
{
	float n300,n100,n50,n0;
  cin >> n300 >> n100 >> n50 >> n0;
  float Accuracy = ((50 * n50) + (100 * n100) + (300 * n300)) / (300 * (n0 + n50 + n100 + n300));
  cout << fixed << setprecision(2);
  cout << Accuracy*100 << "%";
	return 0;
}