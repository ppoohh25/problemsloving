#include <iostream>
using namespace std;

#include <iomanip>
#include <locale>

template<class T>
string FormatWithCommas(T value)
{
    stringstream ss;
    ss.imbue(locale(""));
    ss << fixed << value;
    return ss.str();
}

int main()
{
	int a,b;
  b = 0;
  cin >> a;
  for(int i = 1;i<=12;i++){
    cout << a << " x " << i << " = " << a*i << endl;
    b += a*i;
  }
  if(b > 1000)
  cout << "รวม : " << FormatWithCommas(b) << ".00";
	return 0;
}