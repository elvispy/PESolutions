//PE
#include<iostream>
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;


int M = 1000000;


typedef unsigned long long int big;



int main(){
    int N = 10;
    int p_partial[N][N];
    // Recursion on the number of groups
    // Pre - fill p_partial
    /*
    for(int r = 0; r < N; r++)
    {
        p_partial[r][1] = floor((r+1)/2);   
        for(int j = r; j < N; j++)
        {   
            p_partial[r][r] = 1;


            if (r == 0) {
                p_partial[j][r] = 1;
            } else if ( r < N - 1) 
            {
                p_partial[r+1][r] = 1;
            }else{
                int s = 0;
                for(int k = 0; k < r; r++)
                {
                    s += p_partial[j-r][k];
                }                
                p_partial[j][r] = s;
            }
        }
    } */

    int n = 5;
    int p = 0;
    for(int l = 0; l < n; l++){
        p += p_partial[n-1][l];
    }
	

	cout << "El resultado es " << p;
	return 0;	
}//end main


