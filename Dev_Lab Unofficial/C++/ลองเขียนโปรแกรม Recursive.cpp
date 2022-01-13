#include <iostream>
using namespace std;

int test(int);

int main()
{
  int n;
  cin >> n;
  cout << test(n);
	return 0;
}

int test(int n){
  if(n < 0){
    return -1;
  }
  else if(n == 0){
    return 1;
  }
  else{
    return test(n-1)+100;
  }
}