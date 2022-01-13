#include <iostream>
#include <cstring>
#include <string>
using namespace std;


int main()
{
  string s;
  getline(cin,s);
  
  int n = s.length();
  
  char a[n+1];
  
  strcpy(a, s.c_str());
  
  int count = 0;
  
  for(int i =0;i<n;i++){
    if(a[i] == ';'){
      count +=1;
    }
  }
  cout << count;
	return 0;
}