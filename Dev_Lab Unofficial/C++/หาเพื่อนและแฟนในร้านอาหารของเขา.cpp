#include <iostream>
using namespace std;


int main()
{
	string s;
  cin >> s;
  if(s == "Lee"){
    cout << "สวัสดีที่รัก";
  }
  else if(s == "Ro"){
    cout << "หวัดดีเพื่อน";
  }
  else{
    cout << "ยินดีต้อนรับคุณ " << s;
  }
	return 0;
}