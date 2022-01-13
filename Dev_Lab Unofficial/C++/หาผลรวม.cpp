#include <iostream>
using namespace std;


int main()
{
  int n,a;
  a = 0;
  cin >> n;
  for(int i = 0;i<=n;i++){
    if(i % 2 == 0){
      a += i*i;
    }
  }
  cout << a;
	return 0;
}