//PE
#include<iostream>
#include<fstream>
#include<cstdlib>
#include<array>

using namespace std;

int main(){
	
	char filename[50] = "miprueba.txt";
	ifstream bucky;
	bucky.open(filename);
	
	if(!bucky.is_open()){
		exit(EXIT_FAILURE);
	}
	int word;
	int *primes;
	bucky >> word;
	cout << word << "\n\n";
	int i = 1;
	while(bucky.good()){

		bucky >> word;
		primes[i] = word;
		i++;
	}
	cout << "\n\n";
	//cout << primes[0];
	bucky.close();
	int res = 0;
	cout << "El resultado es: " << res;
	return 0;
}
