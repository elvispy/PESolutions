//PE401
#include<iostream>
#include<math.h>
#include<iomanip>
typedef long long int tipo;

using namespace std;
tipo n = pow(10, 15);
tipo mod = (tipo) pow(10, 9);
tipo lacon = 666666667;

tipo sumsq(tipo num, tipo k){
	tipo e1 = ceil((num+0.5)/(k+1))-1;
	
	
	e1 = e1%mod;
	tipo val1 = ((tipo)(e1*(e1+1)/2)) % mod;
	val1 = ((2*e1+1)* val1)%mod;
	val1 = (val1 * lacon)%mod;
	
	tipo e2 = ceil((num+0.5)/k) - 1;
	e2 = e2%mod;
	tipo val2 = ((tipo)(e2*(e2+1)/2)) % mod;
	val2 = ((2*e2+1)* val2)%mod;
	val2 = (val2 * lacon)%mod;
	
	
	
	tipo res = (k*(val2-val1+mod))%mod;
	
	//cout << res << "\n";
	return res;
}//end sumsq definition
/*
tipo sums(tipo l){
	tipo res = l*(l+1);
	res = res%mod;
	res = ((tipo) res * (2*l+1)/6)%mod;
	return res;
}
*/
tipo sigma2(tipo in1){
	tipo res = 0;
	tipo aux = (tipo) sqrt(in1);
	for(tipo i = 1; i<=aux; i++){
		res+= sumsq(in1, i);
		res = res%mod;
	}//end first for, for sumsq
	
	aux = ceil((in1+0.5)/(aux+1));
	
	for(tipo i = 1; i<aux; i++){
		tipo miaux = ((tipo) in1/i)%mod;
		miaux = (miaux * i)%mod;
		miaux = (miaux * i)% mod;
		res+= miaux;
		res = res%mod;
	}//end second for

	return res;
}//end sigma2 definition
int main(){
	/*
	for(tipo i = 1; i < 10; i++){
		cout << sumsq(n, i) << "\n";
	}
	*/
	cout << "\nEl resultado es: " << sigma2(n);
	return 0;
}
