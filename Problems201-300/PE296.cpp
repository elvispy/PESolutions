//PE296
#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;
/*
def farey_sequence(n: int, descending: bool = False) -> None:
    """Print the n'th Farey sequence. Allow for either ascending or descending."""
    (a, b, c, d) = (0, 1, 1, n)
    if descending:
        (a, c) = (1, n - 1)
    print("{0}/{1}".format(a, b))
    while (c <= n and not descending) or (a > 0 and descending):
        k = (n + b)/d;
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        print("{0}/{1}".format(a, b))
        
*/

int main(){
	int N = 10;
	int a = 0, b = 1, c = 1, d = N;
	int k = 0;
	int aux1, aux2;
	while (c<=N){
		k = (N+b)/d;
		aux1 = c;
		aux2 = d;
	
		c = k*c-a;
		d = k*d-b;
		a = aux1;
		b = aux2;
		cout << a << "/" << b << "\n";
	}
	int res = 0;

	cout << "El resultado es " << res;
	return 0;	
}//end main


