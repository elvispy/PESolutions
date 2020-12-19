//PE733
#include<iostream>
#include<stdio.h>
#include<vector>
#define M (10000019)
#define P (1000000007)
#define N (1000000)

using namespace std;

typedef unsigned long long int big;



int main(){
		
	vector<big> a_is = {};
	vector<int> b_is = {};
	vector<int> c_is = {};
	vector<int> counter = {};
	
	a_is.reserve(1000000);
	b_is.reserve(1000000);
	c_is.reserve(1000000);
	
	counter.reserve(M);
	big last = 153;
	for (int i = 0; i<N; i++){
		if (i%10000 ==0) {
			cout << i << "\n";
		}
		a_is.push_back(last);
		last = (last*153)%M;
		for(int j = 0; j < i; j++){
			if(a_is[j] < a_is[i]){
				b_is[i]++;
				c_is[j]++;
			}
		}
		
		
	}
	int res = 0;

	//cout << "El resultado es " << a_is[3] << " " << a_is.size();
	return 0;	
}//end main


