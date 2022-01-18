#include <iostream>
using namespace std;


int main()
{
	int n;
  cin >> n;
  if(n == 1){
    cout << "OK! Wait please" << endl << "---------------" << endl << "Lift is arriving!" << endl << "---------------"<< endl << "Lift is going up!"<< endl << "---------------"<< endl << "Lift has reached the " << n << "st floor!";
  }
  else if(n == 2){
  	cout << "OK! Wait please" << endl << "---------------" << endl << "Lift is arriving!" << endl << "---------------"<< endl << "Lift is going up!"<< endl << "---------------"<< endl << "Lift has reached the " << n << "nd floor!";
  }
  else if(n == 3){
    cout << "OK! Wait please" << endl << "---------------" << endl << "Lift is arriving!" << endl << "---------------"<< endl << "Lift is going up!"<< endl << "---------------"<< endl << "Lift has reached the " << n << " rd floor!";
  }
  else if(n == 4){
    cout << "OK! Wait please" << endl << "---------------" << endl << "Lift is arriving!" << endl << "---------------"<< endl << "Lift is going up!"<< endl << "---------------"<< endl << "Lift has reached the " << n << "th floor!";
  }
  else if(n == 5){
    cout << "OK! Wait please" << endl << "---------------" << endl << "Lift is arriving!" << endl << "---------------"<< endl << "Lift is going up!"<< endl << "---------------"<< endl << "Lift has reached the " << n << "th floor!";
  }
  else{
    cout << "Error! Not have this floor";
  }
	return 0;
}