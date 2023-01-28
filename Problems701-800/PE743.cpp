//PE743
#include<iostream>
#include<stdio.h>
#include<vector>
#define ll unsigned long long int 
using namespace std;
typedef unsigned long long int big;
const big M = 100007; // Mod
big factorialNumInverse[M] = {};
big fact[M] = {};
big naturalNumInverse[M] = {};

// Function to precompute inverse of numbers
void InverseofNumber()
{
    naturalNumInverse[0] = naturalNumInverse[1] = 1;
    for (int i = 2; i < M; i++)
        naturalNumInverse[i] = naturalNumInverse[M % i] * (M - M / i) % M;
}
// Function to precompute inverse of factorials
void InverseofFactorial()
{
    factorialNumInverse[0] = factorialNumInverse[1] = 1;
 
    // precompute inverse of natural numbers
    for (int i = 2; i < M; i++)
        factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % M;
}
 

// Function to calculate factorial of 1 to N
void factorial()
{
    fact[0] = 1;
 
    // precompute factorials
    for (int i = 1; i < M; i++) {
        fact[i] = (fact[i - 1] * i) % M;
    }
}
int main(){
	
	big k = 100000000;
	big j = 0;
	factorial();
	InverseofNumber();
	InverseofFactorial();
	
	int res = 0;
	for(ll i = 0; i < 10; i++)
		cout << "El resultado es " << fact[i] << "\n";
	return 0;	
}//end main


