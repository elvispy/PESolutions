
#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

int main(){
	
	FILE *f;
	FILE *f2;
		
	int val = 0;
	int i = 0;
	vector<unsigned int>primes = {};
	primes.reserve(10000000);
		
	if((f = fopen("primes1.txt", "r")) != NULL)
	{
	while(!(feof(f)))
	{
		fscanf(f, "%i", &val);
		primes[i] = val;
		i++;
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
		
	fclose(f);
	

	return 0;	
}//end main


