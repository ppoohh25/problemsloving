#include <iostream>
#include <string>
#include <cctype>
using namespace std;


int main()
{
	string s;
  int a,b = 0;
  getline(cin,s);
  for(int i = 0;i<s.length();i++){
    if(isupper(s[i])){
      a+=1;
    }
    else if(islower(s[i])){
      b+=1;
    }
  }
  cout << "UPPER:" << a << endl;
  cout << "LOWER:" << b;
	return 0;
}