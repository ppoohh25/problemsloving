#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main()
{
  int i;
  int a[10];
  int b = 0;
  while(true){
    cin >> i;
    if(i == 0){
      break;
    }
    else{
      a[b] = i;
    	b+=1;
    }
  }
  int c[b];
  
  string s;
  cin >> s;
  /*cout << s << endl;*/
  
  for(int x = 0;x<b;x++){
    c[x] = a[x];
    /*cout << c[x] << endl;*/
  }
  if(s == "Min" || s == "min"){
    sort(c,c+b);
  for(int x = 0;x<b;x++){
    cout << c[x] << " ";
  }
  }
  else{
    sort(c, c + b, greater<int>());
    for(int x = 0;x<b;x++){
    cout << c[x] << " ";
  }
	return 0;
}
}