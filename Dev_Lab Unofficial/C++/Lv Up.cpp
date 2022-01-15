#include <iostream>
#include <string>
using namespace std;


int main()
{
	string a;
  int exp;
  cin >> a >> exp;
  int maxexp,atk,hp,lv;
  lv = 1;
  maxexp = lv*100;
  atk = lv*10;
  hp = lv*100;
  
  
  while(exp >= maxexp){
    exp -= maxexp;
    lv +=1;
    maxexp = lv*100;
  	atk = lv*10;
  	hp = lv*100;
  }
  cout << "Lv : " <<lv << endl;
  cout << "Exp : " <<exp << "/" << maxexp << endl;
  cout << "ATK : " <<atk << endl;
  cout << "HP : " <<hp << endl;
	return 0;
}