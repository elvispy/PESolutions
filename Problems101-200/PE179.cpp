//PE179
#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
#define N (664579)
#define M (10000000)
using namespace std;

vector<unsigned int>primes = {};

class natural
{
public:
	explicit natural (unsigned int n, unsigned int maxx)
	: n( n ), maxx( maxx )
	{
		lis.reserve(N);
		for(unsigned int i = 0; i < N; i++){
			lis.push_back(0);
		}//end for
	}//end explicit definition
	
	void nextt(){
		int idx = 0;
		while(primes[idx] * n > maxx){
			n = n / pow(primes[idx], lis[idx]);
			lis[idx] = 0;
			idx += 1;
		}//end while
		n *= primes[idx];
		lis[idx] += 1;
	}//end nextt definition
	
	unsigned int getn() const{
		return n;
	}//end getVal
	
	unsigned int getidx(unsigned int idx){
		return lis[idx];
	}
	
private:
	unsigned int n;
	unsigned int maxx;
	vector <unsigned int> lis = {};
};//end natural class definition

unsigned int n_div(natural l){
	unsigned int aux = l.getn();
	unsigned int idx = 0;
	unsigned int res = 1;
	while(aux > 1){
		unsigned int expo = l.getidx(idx);
		res *= (expo + 1);
		aux /= pow(primes[idx], expo);
		idx += 1;
	}//end while
	return res;
}

int main(){
	
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
		i++;
		}//end while
	}//en if
	else printf("\nError al abrir el archivo\n");
		
	fclose(f);
	
	natural l(1, M);
	int test = 0;
	for(unsigned int i = 0; i < 1000; i++){
		test = n_div(l);
		l.nextt();
	}
	int res = 0;
	
	cout << "El resultado es " << primes.size();
	return 0;		
}//end main


