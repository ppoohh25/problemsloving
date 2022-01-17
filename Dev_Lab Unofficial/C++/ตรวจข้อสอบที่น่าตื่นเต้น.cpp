#include <iostream>
using namespace std;


int main()
{
	int n,k,m,p,score;
  score = 0;
  string fi,se;
  cin >> n >> k >> m >> p;
  cin >> fi >> se;
  for(int i = 0;i<n;i++){
    if(se[i] == fi[i]){
			score += k;
    }
    else if(se[i] == 'X'){
      score += p;
    }
    else if(se[i] != fi[i] and se[i] != 'X'){
      score -= m;
    }
  }
  cout << "Your score:" << score;
	return 0;
}