//PE70
#include<iostream>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<cmath>
#define M (10000000)
#define N (348513)
// 664579
using namespace std;

typedef unsigned long long int big;

vector<unsigned int> primes = {};
vector<unsigned int> decoms = {1};

int next(vector<unsigned int>&, big);
int phin(vector<unsigned int>&, big);
bool is_perm(string, string);

float minn = 4.0;

int main(){
	//High running time. I am not aware if we can theoretically discard those
	//slow cases. The partial solution is n = 8319823, with n/phi(n) = 1.00071
	//Which is quite low.
	
	decoms.reserve(N);
	primes.reserve(N);
	
	int res = 0; //this is going to be the result
	
	
	for(unsigned int i = 1; i < N; i++){
		decoms.push_back(0); //this will represent the number n
	}
	FILE *f;
	int val = 0;
	if((f = fopen("D:\\GITRepos\\PESolutions\\primes1.txt", "r")) != NULL)
	{
		while(!(feof(f)))
		{
		fscanf(f, "%i", &val);
		if(val > M/2)
			break;
		primes.push_back(val);
		
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
	
	big current = 2;//n
	
	int phi = 1; //phi(n)
	int counter = 0;
	while(decoms[N-1] == 0){
		//cout << current << "\n";
		if(counter%100000 == 0){
			cout << counter << " " << res << "\n";
		}
		phi = phin(decoms, current);
		
	
		if (is_perm(to_string(current), to_string(phi))){
			
			if (((float) current/phi) < minn){
				minn = (float) current/phi;
				res = current;
			}//end inner if

		}//end outer if
		current = next(decoms, current);
		counter++;
	}//end while
	
	
	cout << "\nEl resultado es " << res;
	return 0;	
}//end main

int next(vector<unsigned int> &vect, big current){
	//This function returns the next number using the decomposition given
	if(vect[N-1] == 1){
		return vect[N-1];
	}
	int carr = 0;
	current = 2 * current;
	vect[0]++;
	
	while (current  > M){
		current = round(current / pow(primes[carr], vect[carr]));
		/*
		if(current == 0){
			cout << "sadly im here\n";
			cout << pow(primes[carr], vect[carr]);
		}
		*/
		vect[carr] = 0;
		vect[carr+1]++;
		current *= primes[carr+1];
		carr++;

		
	}//end while
	return current;
	
}//end function definition

bool is_perm(string a, string b){
	//this function check whether a is a permutation of b
	vector<int>a1 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	vector<int>a2 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	for(char el:a){
		a1[(int) el - 48]++;
	}//end for
	for(char el:b){
		a2[(int) el - 48]++;
	}//end for
	
	for(int i = 0; i < 10; i++){
		if (a1[i] != a2[i])
			return false;
	}//end for
	return true;
}//end function definition

int phin(vector<unsigned int> &decoms, big current){
	//this function calculates phi(n) given its decomposition
	int phi = 1;
	int idx = 0;
	

	while(current > 1){
		if (decoms[idx] > 0){
			phi *= pow(primes[idx], decoms[idx] - 1) * (primes[idx] - 1);
			current /= pow(primes[idx], decoms[idx]);
		}//end if
		idx++;

	}//end while
	
	
	return phi;
}//end function definition
