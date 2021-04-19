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
	fillSieve(100000000000);
	cout << isPrime(2013);
	return 0;
}
