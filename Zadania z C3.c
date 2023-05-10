#include<stdio.h>
#include<stdlib.h>

int sumuj2(int **t,unsigned int n, unsigned int m)
{
    int i,j;
    int S = 0;
    int max = 0;
    int indeks = 0;
    for(int i =0;i<n;i++)
    {
        S=S+t[i][j];
    }
    if(i==0)
    {
        max=S;
    }
    if(max<S)
    {
        max=S;
        indeks=i;
    }
    return indeks;
}

int sumuj2(int **t,unsigned int n, unsigned int m)
{
    int i,j;
    int S = 0;
    int max = 0;
    for(int i =0;i<n;i++)
    {
        S=S+t[i][j];
    }
    if(i==0)
    {
        max=S;
    }
    if(max<S)
    {
        max=S;
    }
    return ((double)(max)/m);
}
/////////////////////
/////////////////////
//////////////////////////
///////////////////////
#include<stdio.h>
#include<stdlib.h>

///cw 6_2_1
int** alokuj(unsigned int n, unsigned int m){
int **t=malloc(n*sizeof(int*));
int i;
for(i=0;i<n;i++)
{
    t[i]=malloc(m*sizeof(int));
}
return t;
}

///cw 6_2_2
int(* alokuj2(unsigned int n, unsigned int m))[]{
return malloc(n*sizeof(int[m]));
}

///cw 6_2_18
void wypisz(int **t, unsigned int n, unsigned int m){
    int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
    printf("%d\t",t[i][j]);
}
printf("\n");
}
}
int sumuj2(int **t,unsigned int n, unsigned int m)
{
    int i,j;
    int S = 0;
    int max = 0;
    int indeks = 0;
    for(int i =0;i<n;i++)
    {
        S=S+t[i][j];
    }
    if(i==0)
    {
        max=S;
    }
    if(max<S)
    {
        max=S;
        indeks=i;
    }
}

void wypisz2(unsigned int n,unsigned int m, int t[][m]){
int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
       printf("%d\t",t[i][j]);
    }
    printf("\n");
}
}

///wczytaj
void wczytaj(int** t, unsigned int n,unsigned int m){
int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
       scanf("%d",&t[i][j]);
    }
}
}

///wczytaj2
void wczytaj2(unsigned int n,unsigned int m, int t[][m]){
int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
       scanf("%d",&t[i][j]);
    }
}
}

int main(){
    ///tablica tablic
      int **t=alokuj(3,3);
    wczytaj(t,3,3);
wypisz(t,3,3);
///tablica dwuwymiarowa
int t2[3][3];
wczytaj2(3,3,t2);
wypisz2(3,3,t2);
///inicjalizacja bez wczytywania
int t3[4][4]={{20,2,5,8},{2,8,31,4},{5,6,7,8},{5,6,7,8}};
wypisz2(4,4,t3);
}

Zadamie 6.2.19
void przepisz(int **t1,int **t2,unsigned int n,unsigned int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
        t2[i][j]=t1[i][j];
        }
    }
}

Zadanie 6.2.20
#include<stdio.h>
#include<stdlib.h>

///cw 6_2_1
int** alokuj(unsigned int n, unsigned int m){
int **t=malloc(n*sizeof(int*));
int i;
for(i=0;i<n;i++)
{
    t[i]=malloc(m*sizeof(int));
}
return t;
}
///cw 6_2_18
void wypisz(int **t, unsigned int n, unsigned int m){
    int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
    printf("%d\t",t[i][j]);
}
printf("\n");
}
}
///wczytaj
void wczytaj(int** t, unsigned int n,unsigned int m){
int i,j;
for(i=0;i<n;i++)
{
    for(j=0;j<m;j++)
{
       scanf("%d",&t[i][j]);
    }
}
}
/// Zadanie 6.2.20
void przepisz(int **t1,int **t2,unsigned int n,unsigned int m)
{
    int temp;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            temp= t2[i][j];
            t2[i][j]=t1[i][j];
            t1[i][j]=temp;
        }
    }
}
int main(){
    ///tablica tablic
      int **t=alokuj(4,3);
      int **t2=alokuj(4,3);
    wczytaj(t,4,3);
wypisz(t,4,3);
wczytaj(t2,4,3);
wypisz(t2,4,3);
przepisz(t,t2,4,3);
printf("\n");
wypisz(t,4,3);
printf("\n");
wypisz(t2,4,3);
}

void odwroc_wiersze(int **t1,unsigned int n,unsigned int m)
{
    int temp;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m/2;j++)
        {
            temp= t1[i][j];
            t1[i][j]=t1[i][m-1-j];
            t1[i][m-1-j]=temp;
        }
    }
}

int main(){
    ///tablica tablic
      int **t=alokuj(3,3);
    wczytaj(t,3,3);
wypisz(t,3,3);
odwroc_wiersze(t,3,3);
wypisz(t,3,3);

}

jakies przesuwanie w tablicach 
o np wiersz w dol 


void wiersze_w_dol(int **t1,unsigned int n,unsigned int m){
    int i,j,pom;
        for(j=0;j<m;j++)
{
    pom=t1[n-1][j];
    for(i = n-1;i>0;i++)
    {
        t1[i][j]=t1[i-1][j];
    }
    t1[0][j]=pom;
}
}






