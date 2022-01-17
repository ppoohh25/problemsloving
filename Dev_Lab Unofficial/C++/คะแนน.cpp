#include <iostream>
using namespace std;


int main()
{
	int n;
  cin >> n;
  if(n <=25 and n >= 0){
    cout << "fail";
  }
  else if(n >=26 and n <= 50){
    cout << "good";
  }
  else if(n >= 51 and n <=75){
    cout << "very good";
  }
  else if(n >= 76 and n <=100){
    cout << "excellent";
  }
	return 0;
}