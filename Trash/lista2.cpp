/*Escribir un programa que permita cargar un valor numerico entero
en una Estructura de datos tipo Lista.
Crear un menu que permita insertar nodos
Borrar Nodos y
Visualizar los datos de la Lista.*/
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

typedef struct elemento{ int x;} ELEMENTO;


typedef struct lista
{
  ELEMENTO Dato;
  struct lista *sig;
}LISTA;

typedef LISTA *pLista;

void insertar(pLista *, ELEMENTO);
void extraer(pLista *);
void visualizar(LISTA *);

main() /* Rellenar, extraer y visualizar */
{
	LISTA *vote_lista_uno = NULL;
	ELEMENTO N;
	char opc;

	do
	{
		system("cls"); /* borramos la pantalla */

    	printf("\t\t1.- Insertar\n");

		printf("\t\t2.- Extraer\n");

		printf("\t\t3.- Visualizar la Lista\n");

		printf("\t\t4.- Salir\n");
		opc=getch();
		switch(opc)
		{
            case '1':
                system("cls");
                printf("Digite un valor entero: ");
                scanf("%d", &N.x);
                insertar(&vote_lista_uno,N);
                break;
            case '2':
                extraer(&vote_lista_uno);
                break;
            case '3':
                visualizar(vote_lista_uno);
		}
	}while (opc!='4');
}

void insertar(pLista *raiz, ELEMENTO X)
{
   LISTA *nuevo;
   nuevo = (LISTA *)malloc(sizeof(struct lista));
   nuevo->Dato= X;
   if ((*raiz)==NULL)
     { (*raiz)=nuevo;
       nuevo->sig=NULL;
     }
   else
     {
       nuevo->sig=(*raiz);
       (*raiz)=nuevo;
     }//endif
}

void extraer(pLista *raiz)
{
   LISTA *aux;

   if(raiz != NULL)
   {
       aux=(*raiz);
       (*raiz) = (*raiz)-> sig;
       free(aux);
       printf("\n\nExtraccion realizada...., pulse una tecla");
   }
   else printf("\n\nNo existen datos a extraer...\n");
   getch();
}

void visualizar(LISTA *raiz)
{
    if (raiz==NULL) printf("\n\nNo existen datos a visualizar...\n");
	else
    {
        system("cls");
	    printf("\n\nValores numericos digitados\n");
        while(raiz!=NULL)
        {
             printf("%d\n",raiz->Dato.x);
	         raiz=raiz->sig;
        }
    }
    system("pause");
}
