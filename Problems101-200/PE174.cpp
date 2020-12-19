//PE174
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
#define N (41538) // 78498 - 41538
#define M (1000000)

using namespace std;

typedef unsigned long long int big;

vector<unsigned int> primes = {};
vector<unsigned int> decoms = {0};
vector<int> types = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int next(vector<unsigned int>&, big);
int type(vector<unsigned int>&, big);

// vector<int> divs(vector<unsigned int> &, big, vector<int>&, int, int);


int main(){
	vector<int> miaux = {};
	
	decoms.reserve(N);
	primes.reserve(N);
	
	// int res = 0;
	
	for(unsigned int i = 1; i <= N; i++){
		decoms.push_back(0); //this will represent the number n
	}
	FILE *f;
	
	int val = 0;
	if((f = fopen("D:\\GITRepos\\PESolutions\\pprimes.txt", "r")) != NULL)
	{
		while(!(feof(f)))
		{
		fscanf(f, "%i", &val);
		if(val > M)
			break;
		primes.push_back(val);
		
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
	
	
	val = 1;
	int counter = 0;
	int Nn;
	while (val != 0){
		val = next(decoms, val);
		Nn = type(decoms, val);
		if (Nn < 11 and Nn > 0){
			counter++;	
		} 
		/*
		if (val == 90000){
			cout << counter << "\n";
			break;
		}*/
	} // end while
	

	cout << "El resultado es " << counter << "\n";
	return 0;
	vector<int> res = divs(decoms, val, miaux, 0, -1);
	for(unsigned int el: res){
		cout << el << "\n";
	}
	
	return 0;	
}//end main


int next(vector<unsigned int> &vect, big current){
	//This function returns the next number using the decomposition given

	
	int carr = 0;
	current = 2 * current;
	vect[0]++;
	
	while (current > M){

		current = round(current / pow(primes[carr], vect[carr]));

		vect[carr] = 0;
		carr++;
		vect[carr]++;
		current *= primes[carr];

	}//end while
	
	if(current == 500009){
		return 0;
	}

	return current;
	
}//end function definition

int type(vector<unsigned int>& decoms, big current){
	if (decoms[0] == 1 or decoms[0] == 0) return 0;
	int res = 1;
	int idx = 0;
	while (current > 1){
		while (decoms[idx] == 0) idx++;
		
		current = (big) (current / pow(primes[idx], decoms[idx]));
		res *= (decoms[idx]+1);
		idx++;
	} // end while
	

	res = (decoms[0] - 1) * ( res / (decoms[0] + 1));
	return floor(res/2.0);
}


/*

vector<int> divs(vector<unsigned int> &decoms, big current, vector<int> &last_divs, int idx, int pot_2){
	if(idx == 0){
		pot_2 = decoms[0];
		current = (big) (current / pow(2, pot_2));
		vector<int> lolazo = {1};
		return divs(decoms, current, lolazo, 1, pot_2);
	}else if (current == 1) {
		vector<int> divss;
		for (int i = 0; i <= pot_2; i++){
			
			for (int el: last_divs){
				divss.push_back((int) (el * pow(2, i)));
			} // end inner for
		} // end outer for
		return divss;
	}else{
		while(decoms[idx] == 0){
			idx++;
		}
		current = (big) (current / pow(primes[idx], decoms[idx]));
		
		vector<int> divss;
		for(int i = 0; i <= decoms[idx]; i++){
			for(int el: last_divs){
				divss.push_back((int) (el * pow(primes[idx], i)));
			}
		}
		
		return divs(decoms, current, divss, idx + 1, pot_2);
	}
}

*/


