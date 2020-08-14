#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace std;
int main()
{
	FILE *f;
	FILE *f2;
	int titulo;
	int valor = 0;
	int suma = 0;
	double prom = 0;
	int i = 0;
	if((f = fopen("miprueba.txt", "r")) != NULL)
	{
		while(!(feof(f)))
		{
			i++;
			fscanf(f, "%i", &valor);
			suma += valor;

		}
	}
	
	else printf("\nError al abrir el archivo\n");
	
	prom = suma / i;
	cout << prom << "\n";
	
	fclose(f);
	return 0;
}

