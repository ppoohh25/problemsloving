#include <iostream>
using namespace std;


int main()
{
  string name;
  string suname;
  int a;
  cin >> name >> suname;
  cin >> a;
  if((2015-a)>18){
    cout << "Welcome " << name << " " << suname << " to NongGipsy Pub";
  }
  else{
    cout << "You shall not pass!";
  }
	return 0;
}