#include <iostream>
using namespace std;


int main()
{
	int n,m,k,A;
  cin >> n >> m >> k >> A;
  int s = 0;
  for(int i = 0;i<m-n+1;i++){
    s+=(k + A*i);
  }
  if(1234-s < 0){
    cout << "YES";
  }
  else{
    cout << 1234-s;
  }
	return 0;
}