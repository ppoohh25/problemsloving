#include <iostream>
using namespace std;


int main()
{
	double boxra,hand,nut,hand_nut,collect;
  collect = 0;
  cin >> boxra >> hand >> nut >> hand_nut;
  
  while(hand < boxra && nut != 0){
    nut -=1;
    hand += hand_nut;
    if(hand > boxra){
      break;
    }
    else{
      collect +=1;
    }
  }
  cout << collect;
	return 0;
}