//PE
#include<iostream>
#include<stdio.h>
#include<vector>
#include<iostream>

typedef unsigned long long int big;
using namespace std;

vector<bool> sieve;

bool isPrime(big x){
	if((x & 1) == 0)
		return x == 2;
		
	return sieve[x >> 1];
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
	
	/*
	We are counting the number of elements of the form
	p = 4k+3
	4p
	16p
	4, 16 are exceptions
	32 is not an exception as it produces two solutions 1, 4, 7 and 5, 8, 11
	*/

	int t1 = 0;
	int t2 = 0;
	int t3 = 0;
	int N = 50000000;
	fillSieve(N);
	for (int i = 0; 2 * i + 1 < N; i++)
	{
		if (sieve[i]){
			//if (i%2 == 1) cout << 2 * i + 1 << " t1 \n";
			if (i%2 == 1) t1++;
			
			//if (4*(2*i+1) < N) cout << 4 * (2 * i + 1)<< " t2 \n";
			if (4*(2*i+1) < N) t2++;
			
			//if (16*(2*i+1) < N) cout << 16*(2 * i + 1) << " t3 \n";
			if (16*(2*i+1) < N) t3++;
			
			
		} //end if (is prime)
		
	} //end for
	
	cout << "El resultado es: " << t1 + t2 + t3 + 2;
	return 0;	
}//end main


