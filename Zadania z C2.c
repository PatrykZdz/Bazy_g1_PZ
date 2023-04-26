Zadanie 5.2.9
#include <stdio.h>
void wytnij(char* napis, int n, int m)
{
    int i,j;
    for(j=0;napis[j]!=0;j++)
    {

    }
    if(j+1>m)
    {
        for(i=0;i+m<j;i++)
        {
            napis[n+i]=napis[m+i+1];
        }
    }
    else if((n<j)&&(j+1<=m))
    {
        napis[n]=0;
    }
}
int main()
{
    char napiszad9[40]="z tego napisu mamy cos wyciac";
    printf(napiszad9);
    printf("\n");
    wytnij(napiszad9,5,15);
    printf(napiszad9);
    char krotki[30]= "krotki";
    printf("\n");
    printf(krotki);
    printf("\n");
    wytnij(krotki,8,12);
    printf(krotki);

    return 0;
}
Zadanie 5.2.10

#include <stdio.h>
#include <stdbool.h>
void wytnij(char* napis, int n, int m)
{
    int i,j;
    for(j=0;napis[j]!=0;j++)
    {

    }
    if(j+1>m)
    {
        for(i=0;i+m<j;i++)
        {
            napis[n+i]=napis[m+i+1];
        }
    }
    else if((n<j)&&(j+1<=m))
    {
        napis[n]=0;
    }
}
bool porownanie(char* napis1,char* napis2,int n)
{
    for(int i =0;(napis1[i]!=0)&&napis2[i]!=0;i++)
    {
        if(napis1[n+1]!=napis2[i])
        {
            return false;
        }
        if(napis2[i]==0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
void wytnij2 (char* napis1,char* napis2)
{
    int i,dl;
    for(int dl = 0;napis2[dl]!=0;dl++){}
        for(int i=0;napis1[i]!=0;i++)
        {
            if(porownanie(napis1,napis2,i))
            {
                wytnij(napis1,i,i+dl-1);
                return;
            }
        }
}

int main()
{
    char napis1[40] = "napis z ktorego ktorego wycinamy";
    char napis2[40] = "ktorego";
}

Zadanie 5.2.13
#include <stdio.h>
#include <stdbool.h>
void wytnijtesameznaki(char* napis1, char* napis2)
{
    int i,j;
    for(i=0,j =0;napis1[i]!=0;i++)
    {
    if(napis1[i]!=napis2[i])
        {
            napis1[j]=napis1[i];
            j++;
        }
    }
    napis1[j]=0;
}
int main()
{
    char napis1[40] = "arbuzek";
    char napis2[40] = "arbiter";
    wytnijtesameznaki(napis1,napis2);
    printf(napis1);
}
Zadanie 5.2.20
#include <stdio.h>
#include <stdbool.h>
char * godzina(int godz,int min,int sek)
{
    char* wynik = malloc(9*sizeof(char));
    sprintf(wynik,"%02d:%02d:%02d",godz,min,sek);
    return wynik;
}
int main()
{
  int godziny = 7;
  int minuty = 59;
  int sekundy = 5;
  printf(godzina(godziny,minuty,sekundy));
}

Zadanie 5.2.26
#include <stdio.h>
#include <stdbool.h>
#include <wchar.h>
#include <string.h>
void duze(char* napis1)
{
  for(int i = 0;napis1[i]!=0;i++)
  {
      napis1[i]=towupper(napis1[i]);
  }
}
int main()
{
    char napis[40] = "elo";
    printf(napis);
    printf("\n");
    duze(napis);
    printf(duze);
}

Zadanie 5.2.22

#include <stdio.h>
#include <stdbool.h>
#include <wchar.h>
#include <string.h>
char* sklejenie(char* napis1,char* napis2,char* napis3)
{
    char*wynik = malloc((strlen(napis1)+strlen(napis2)+strlen(napis3)+1)*sizeof(char));
    strcpy(wynik,napis1);
    strcat(wynik,napis2);
    strcat(wynik,napis3);
    return wynik;
}

int main()
{
    char* napisa="arbuz";
    char* napisb="baobab";
    char* napisc="czekolada";
    char*napiswynik;
    napiswynik=sklejenie(napisa,napisb,napisc);
    printf(napiswynik);
}

Zadanie 6.2.1
int** alokuj(unsigned int n, unsigned int m)
{
    int **t=malloc(n*sizeof(int*));
    for(int i= 0; i<n;i++)
    {
        t[i]=malloc(m*sizeof(int));
    }
    return t;
}

Zadanie 6.2.2

int(*alokuj2(unsigned int n ,unsigned int m))[]
{
    return malloc(n*sizeof(int[m]));
}


Zadanie 6.2.18
void wypisz(int **t,unsigned int n, unsigned int m)
{
    for(int i = 0; i <n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            printf("%d\t",t[i][j]);
        }
    printf("\n");
    }
}

void wypisz2(unsigned int n, unsigned int m, int t[][m])
{
    for(int i = 0; i<n;i++)
    {
        for (int j = 0; j<n;j++)
        {
            printf("%d\t",t[i][j]);
        }
    }
    printf("\n");
}

void wczytaj(int **t,unsigned int n,unsigned int m)
{
    for (int i= 0; i<n;i++)
    {
        for(int j = 0; j<m;j++)
        {
            scanf("%d",t[i][j]);
        }
    }
}

#include <stdio.h>
#include <stdbool.h>
#include <wchar.h>
#include <string.h>

int** alokuj(unsigned int n, unsigned int m)
{
    int **t=malloc(n*sizeof(int*));
    for(int i= 0; i<n;i++)
    {
        t[i]=malloc(m*sizeof(int));
    }
    return t;
}

int(*alokuj2(unsigned int n ,unsigned int m))[]
{
    return malloc(n*sizeof(int[m]));
}

void wypisz(int **t,unsigned int n, unsigned int m)
{
    for(int i = 0; i <n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            printf("%d\t",t[i][j]);
        }
    printf("\n");
    }
}
void wypisz2(unsigned int n, unsigned int m, int t[][m])
{
    for(int i = 0; i<n;i++)
    {
        for (int j = 0; j<n;j++)
        {
            printf("%d\t",t[i][j]);
        }
    }
    printf("\n");
}
void wczytaj(int **t,unsigned int n,unsigned int m)
{
    for (int i= 0; i<n;i++)
    {
        for(int j = 0; j<m;j++)
        {
            scanf("%d",t[i][j]);
        }
    }
}

void wczytaj2(unsigned int n, unsigned int m, int t[][m])
{
    for (int i= 0; i<n;i++)
    {
        for(int j = 0; j<m;j++)
        {
            scanf("%d",t[i][j]);
        }
    }
}
int main()
{
        int **t=alokuj(3,3);
    wczytaj(t,3,3);
wypisz(t,3,3);

int t2[3][3];
wczytaj2(3,3,t2);
wypisz2(3,3,t2);

int t3[4][4]={{20,2,5,8},{2,8,4,31},{5,6,7,8},{5,4,3,2}};
wypisz2(4,4,t3);
}

Zadanie 6.2.3

void zwolnij(unsigned int n, unsigned int m, int **t)
{
    for(int i =0;i<n;i++)
    {
        free(t[i]);
    }
    free(t);
}

void zwolnij2(unsigned int n, int t[][n])
{
    free(t);
}

Zadanie 6.2.7

int **alokuj(unsigned int n, unsigned int m)
{
    int**t=malloc(n*sizeof(int*));
    for(int i = 0; i <n;i++)
    {
        t[i]=malloc((i+1)*sizeof(int));
    }
    return t;
}



