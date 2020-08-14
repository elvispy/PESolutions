//PE528
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;

int bi_search(vector<unsigned int> &, int, int, unsigned int, int);

int main(){
	
	FILE *f;
	FILE *f2;
		
	int val = 0;
	int i = 0;
	int N = 100;
	vector<unsigned int>primes = {};
	primes.reserve(10000000);
		
	if((f = fopen("D:\\GITRepos\\PESolutions\\2T_part1.txt", "r")) != NULL)
	{
	while(!(feof(f)) and val < N)
	{
		fscanf(f, "%i", &val);
		primes[i] = val+1;
		i++;
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
	
	int len = i-1;
	//cout << bi_search(primes, len, 18);
	fclose(f);
	cout << "Comenzando...\n";
	
	long long int res = 0;
	for(int j = 2; j <= len; j++){
		for(int k = 0; k<=j-1; k++){
			if(primes[j]%primes[k] == 0){// and aux/miaux < N){
				cout << primes[k]-1 << " " << primes[j]-1 << "\n";
				float aux = sqrt(primes[j] * primes[k]);
				if(aux == (int) aux){
					aux = (int) aux;
					int pos = bi_search(primes, k, j, aux, k+1);
					if(pos != -1){
						//cout << primes[k]-1 << " " << primes[pos]-1 << " " << primes[j]-1 << "\n";
						res += primes[k] + primes[j] + primes[pos] - 3;
					}//end inner if
				}//end inner if
			}//end if
		}//end inner for
	}//end for
	
	cout << "El resultado es " << res;
	return 0;	
}//end main

int bi_search(vector<unsigned int> &primes, int min, int max, unsigned int elem, int guess = 0){

	while(min <= max){
		//cout << guess << "\n";
		if(primes[guess] == elem){
			return guess;
		}else if(primes[guess] > elem){
			max = guess-1;
			guess = (int) ((max + min)/2);
		}else if (primes[guess] < elem){
			min = guess+1;
			guess = (int) ((max + min + 1)/2);
		}
	}//end while
	return -1;
	
}//end function definition


