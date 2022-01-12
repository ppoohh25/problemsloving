#include <iostream>
#include<string>
#include <bits/stdc++.h>
using namespace std;


int main()
{
  int a,b,a_b;
  cin >> a;
  cin >> b;
  a_b = a+b;
  string n = to_string(a_b);
  reverse(n.begin(), n.end());
  cout << n;
	return 0;
}