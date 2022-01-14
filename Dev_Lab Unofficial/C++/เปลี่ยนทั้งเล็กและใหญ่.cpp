#include <iostream>
#include <cstring>
#include <cctype>
using namespace std;


int main()
{
	string s;
  getline(cin,s);
 
  int n = s.length();
 
   
  char char_array[n + 1];
 
  strcpy(char_array, s.c_str());
  for(int i = 0;i<n+1;i++){
    if(isupper(char_array[i])){
      char_array[i] = tolower(char_array[i]);
    }
    else if(islower(char_array[i])){
      char_array[i] = toupper(char_array[i]);
    }
  }
  cout << char_array;
	return 0;
}