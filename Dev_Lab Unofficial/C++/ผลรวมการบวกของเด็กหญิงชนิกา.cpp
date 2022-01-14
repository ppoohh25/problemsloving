#include <iostream>
using namespace std;



int main()
{
  int n,a;
  a = 0;
  cin >> n;
  for(int i = 1;i<=n;i++){
    a +=i;
  }
  cout << a;
	return 0;
}