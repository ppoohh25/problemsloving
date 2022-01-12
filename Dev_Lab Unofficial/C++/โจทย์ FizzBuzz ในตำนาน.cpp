#include <iostream>
using namespace std;


int main()
{
	int n;
  cin >> n;
  if(n%3 == 0 && n%2==0){
    cout << "FizzBuzz";
  }
  else if(n %2 == 0){
    cout << "Buzz";
  }
  else if(n % 3 == 0){
    cout << "Fizz";
  }
	return 0;
}