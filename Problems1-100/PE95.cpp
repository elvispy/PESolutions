//PE95
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>


typedef unsigned long long int big;
using namespace std;

big n_div(big n);

vector<bool> sieve;
vector<int> primes;
//vector<int

bool isPrime(int x){
	if((x & 1) == 0)
		return x == 2;
		
	return sieve[x >> 1];
}//end function definition


int isin(vector<big> &temporal, int val){
	for(big j = 0; j < temporal.size(); j++){
		if(temporal[j] == val){
			return temporal.size() - j;
		}//end if
	}//end for
	return 0;
}//end function definition


int elmin(vector<big> &temporal, int elaux){
	int tam = temporal.size();
	int res = temporal[tam - elaux];
	for(int i = tam - elaux; i < tam; i++){
		if(temporal[i] < res){
			res = temporal[i];
		}//end if
	}//end for
	
	return res;
}//end function definition

void fillSieve(big size){
	//store only odd numbers
	const unsigned int half = (size >> 1) + 1;
	//allocate memory
	sieve.resize(half, true);
	
	sieve[0] = false;
	
	for (big i = 1; 2*i*i < half; i++)
	{
		if (sieve[i])
		{
			unsigned int current = 3*i+1;
			while(current < half){
				sieve[current] = false;
				current += 2*i+1;
			}//end while
		}//end if
	}//end for
}//end function definition


int main(){
	
	vector<big> nextt = {}; //vector with
	
	nextt.reserve(1000000);
	nextt.push_back(0);
	sieve.reserve(1000000);
	fillSieve(1000000);
	
	for(int i = 1; i <= 1000000; i++){
		if(isPrime(i)){
			primes.push_back(i);
			nextt.push_back(1);
		}else{
			nextt.push_back(n_div(i));
		}//end if
	}//end for for primes and nextt

	cout << "Im finished calculating stuff\n";
	
	int maxcycle = 0;
	int sig = 0;
	int elaux = 0;
	int res = 0;
	vector<big> temporal = {};
	for(int j = 2; j<= 1000000; j++){
	 	//cout << j << "\n";
	 	if (nextt[j] != 0){
	 		sig = nextt[j];
	 		temporal.push_back(j);
	 		while(sig <= 1000000 and sig != 0){
	 			elaux = isin(temporal, sig);
	 			if(elaux == 0){
	 				temporal.push_back(sig);
	 				sig = nextt[sig];
				 }else{
				 	if(maxcycle < elaux){
				 		maxcycle = elaux;
				 		res = elmin(temporal, elaux);
				 		/*
				 		for(int i =0; i < temporal.size(); i++)
				 			cout << temporal[i] << "\n";
				 		cout << j << " " << maxcycle<< "\n--------\n";
				 		*/
					 }//end inner if
					 break;
				 }//end outer if
			 }//end while
			 for(big temp: temporal){
			 	nextt[temp] = 0;
			 }//end for
			 temporal = {};

	 	}//end if
	}//end for
	
	cout << res;
	
	return 0;	
}//end main

big n_div(big n){
	if(n <= 1){
		return 0;
	}/*else if(isPrime(n)){
		return 1;
	}//end if*/
	big res = 1;
	big miaux = n;
	big idx = 0;
	big exp = 0;
	while (n > 1){
		if(primes[idx] > n){
			break;
		}//end if
		exp = 0;
		while (n%primes[idx] == 0){
			exp+=1;
			n = (big) (n/primes[idx]);
			
		}//end inner while
		res *= (big) (pow(primes[idx], exp+1) - 1);
		res /= primes[idx] -1;
		idx +=1;
	}//end outer while
	
	
	return res-miaux;
}

