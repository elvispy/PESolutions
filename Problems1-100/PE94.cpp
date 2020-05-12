#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
typedef long long int tipo;
//setprecision(20);
const double r3 = 1.7320508075688772935274463415058723669428052538104;

bool satisfies(tipo x){
	tipo val = (tipo) (x*r3) +1;
	tipo val2 = 3*x*x+2*x-1;
	if (val*val == val2){
		return true;
	}else{
		return false;
	}	
}

bool satisfies2(tipo x){
	tipo val = (tipo) (x*r3);
	tipo val2 = 3*x*x-2*x-1;
	if (val * val == val2){
		return true;
	}
	return false;
}

int main(){
	tipo x = 3;
	long int res = 0;
	while(x <= 333333333){
		
		if (satisfies(x)){
			res += 3*x-1;
		}
		
		if (satisfies2(x)){
			res += 3*x+1;
		}//end second if
		
		x = x + 2;
	} //end while
	cout << "El resultado es : " << res;
	return 0;
}
