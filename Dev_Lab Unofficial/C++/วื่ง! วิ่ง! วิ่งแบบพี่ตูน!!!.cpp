#include <iostream>
using namespace std;


int main()
{
  int a,b,c;
  c = 0;
  cin >> a >> b;
  for(int i =1;i<=a;i++){
    cout << i << "-" << b << endl;
    c+= b;
  }
  cout << c;
	return 0;
}