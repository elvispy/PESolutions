//PE179
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
#define N (664579)
#define M (10000000)   

using namespace std;

typedef unsigned long long int big;

vector<unsigned int>primes = {};
vector<unsigned int> already = {1};
vector<unsigned int> decoms = {0, 1};

int main(){
	
	decoms.reserve(M);
	for(unsigned int i = 1; i < M; i++){
		decoms.push_back(0);
	}
    FILE *f;
		
	int val = 0;
	int i = 0;
	
	primes.reserve(N);
		
	if((f = fopen("D:\\GITRepos\\PESolutions\\primes1.txt", "r")) != NULL)
	{
	while(!(feof(f)))
	{
		fscanf(f, "%i", &val);
		if(val > M)
			break;
		primes.push_back(val);
		if(val > 3162){
			if(val < M/2){
				already.push_back(val);
			}
			decoms[val] = 2;
		}
		i++;
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
		
	fclose(f);

	//Now lets complete the decoms
	big aux = 0;
	int expo = 1;
	big k = 0;
	vector<unsigned int> cache = {};
	for(unsigned int j = 445; j >= 1; j--){
		for(unsigned int idx = 0; idx < already.size(); idx += 1){
			k = already[idx];
			aux = k * primes[j];
			expo = 1;
			while(aux <= M){
				decoms[aux] = decoms[k] * (expo + 1);
				
				
				//to avoid overflow with big
				if(aux <= M/2){
					cache.push_back(aux);
				}
				aux *= primes[j];
				expo += 1;
			}//end while
		}//end inner for
		for(unsigned int l: cache){
			already.push_back(l);
		}//end for
		cache = {};
	}//end for
	
	//i need to treat p = 2 differently, for some reason
	for(unsigned int j = 1; j <= M/2; j += 2){
		aux = 2*j;
		expo = 1;
		while(aux <= M){
			decoms[aux] = decoms[j] * (expo + 1);
			expo += 1;
			aux *= 2;
		}
	}//end for
	
	//Now lets count the number of coincidences
	int res = 0;
	for(big i = 2; i < M; i++){
		if(decoms[i] == decoms[i+1])
		{
			res +=1;
		}//end if		
	}//endfor

	cout << "El resultado es: " << res;
	return 0;	
}// end main


