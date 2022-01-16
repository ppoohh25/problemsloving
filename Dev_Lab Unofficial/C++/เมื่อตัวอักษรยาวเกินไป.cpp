#include <iostream>
#include <string>
using namespace std;


int main()
{
	string s;
  int n;
  getline(cin,s);
  cin >> n;
  if(s.length() > n){
    for(int i = 0;i<n;i++){
      cout << s[i];
    }
    cout << "...";
  }
  else{
    cout << s;
  }
	return 0;
}