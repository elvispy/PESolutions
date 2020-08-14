//PE153
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>

typedef unsigned long long int big;
using namespace std;

int gcd( int c1, int d1){
	if(c1 == 0){
		return d1;
	}
	return gcd(d1%c1, c1);
}

int main(){
	/*Find solutions to the equations c*c + d*d divides ac and c*c + d*d divides a*d*/
	
	int N = pow(10, 8);
	
	
	//First we handle the case d = 0 seperataly
	big res = 0;
	
	for(int i = 1; i <= N; i++){
		res += i * (((int) N/i ));
		//cout << i * ( (int) N/i) << "\n";
	}//end for


	//the case c1 = d1 = 1 is handled separately, also
	for(int m = 1; m<=N/2; m++){
		res += 2*m *( (int) N/(2*m));
	}//end for
	
	for(int c1 = 1; c1 <= sqrt(N/2); c1++){
		for(int d1 = c1 + 1; c1*c1 + d1*d1 <= N; d1++){
			if(gcd(c1, d1) == 1){
				//cout << c1 << " " << d1 << "\n";
				for(int m = 1; m<= N/((c1*c1 + d1*d1)); m++){
					res += 2*m*(c1 + d1) * ((int) N/(m * (c1*c1 + d1*d1)));
					
				}//end inner (m) for
			}
		}//end inner (d1) for
	}//end outer (c1) for
	
	cout << "El resultado es " << res;
	return 0;	
}//end main


