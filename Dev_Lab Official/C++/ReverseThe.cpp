#include <iostream>
using namespace std;


int main()
{	
  string a[100];
  string temp;
  for(int i = 0;i<100;i++){
    cin >> a[i];
  }
   for ( int i = 0, j = 100 - 1; i < 100/2; i++, j--)  
    {     
        temp = a[i];  
        a[i] = a[j];  
        a[j] = temp;  
    }
  for(int i = 0;i<100;i++){
    if(a[i] != ""){
       cout << a[i] << " ";
    }
  }
	return 0;
}