/// Wstep 
printf("%d\n",'a');
    printf("%d\n",'A');
    printf("%d\n",'1');

    void wyczysc(char* napis)
    {
        napis[0]=0;
    }
    char *napis = "pieczewo";
    printf(napis);
    printf("\n");
    printf("Po wyczszczeniu");
    wyczysc(napis);
    printf(napis);

    free(napis);


/// Dlugosc napisu
int main()
{
    int dlugosc(char* napis)
    {
        int i = 0;
        while(napis[i]!=0)
            i++;
        return i;
    }

    char *napis = "pieczewo";
    printf(napis);
    printf("\n");
    printf("%d",dlugosc(napis));
    return 0;
}

/// Dlugosc napisu
int main()
{
    int dlugosc(char* napis)
    {
        int pom=0;
        int i = 0;
        while(napis[i]!=0)
        {
            if(napis[i]!=32)
            pom++;
            i++;
        }
        return pom;
    }

    char *napis = "Programowanie strukturalne to bardzo przyjemny przedmiot";
    printf(napis);
    printf("\n");
    printf("%d",dlugosc(napis));
    return 0;
}

/// Zdanie połączeniu
int main()
{
    int dlugosc(char* napis)
    {
        int pom=0;
        int i = 0;
        while(napis[i]!=0)
        {
            if(napis[i]!=32)
            pom++;
            i++;
        }
        return pom;
    }
    char *napis = "Programowanie strukturalne to bardzo przyjemny przedmiot";
    printf(napis);
    printf("\n");
    printf("%d",dlugosc(napis));
    return 0;
}

/// Zdanie Porownanie
int main()
{
    int dlugosc(char* napis)
    {
        int pom=0;
        int i = 0;
        while(napis[i]!=0)
        {
            if(napis[i]!=32)
            pom++;
            i++;
        }
        return pom;
    }
    char *napis = "Kot";
    char *napis2 = "Elo";
    int porownajmynapisy(char *napis, char *napis2)
    {
        int i;
        int dll= dlugosc(napis);
        int dl2= dlugosc(napis2);
        if(dll==dl2)
        {
            for(i=0 ; i<=dl2;i++)
            {
                if(napis[i]!=napis2[i])
                {
                    return 0;
                }
                else
                {
                    return 1;
                }
            }
        }
    }
    printf("%d\n",porownajmynapisy(napis,napis2));
    return 0;
}


/// Zdanie Porownanie w Slowniku
int main()
{
    int porownajslownik(char* napis1, char* napis2)
    {
        int i,x;
        for(i =0;napis1[i]||napis2[i];i++)
        {
            if(napis1[i]==0 && napis2[i]==0)
            {
                return 0;
            }
            if(napis1[i]!=0 && napis2[i]==0)
            {
                return 1;
            }
            if(napis1[i]==0 && napis2[i]==0)
            {
                for(x=0;napis1[x];x++)
                {
                    if(napis1[x]<napis2[x]==0)
                    {
                        return 0;
                    }
                }
            }

        }
    }
    printf("%d",porownajslownik("ala","tata"));
    return 0;
}


/// Zdanie Przepisanie z jednego do drugiego
int main()
{
    int dlugosc(char* napis)
    {
        int i = 0;
        while(napis[i]!=0)
            i++;
        return i;
    }
    void przepisz(char*napis1,char*napis2)
    {
        for(int i = 0;i<dlugosc(napis1);i++)
        {
            napis2[i]=napis1[i];
        }
            napis2[dlugosc(napis1)]=0;
    }

    void wypisz(char*napis)
    {
        printf("%s",napis);
    }
    char*pierwszy = "arbuz";
    char drugi[20] = "arbiter";
    wypisz(pierwszy);
    printf("\n");
    wypisz(drugi);
    przepisz(pierwszy,drugi);
    printf("\n");
    wypisz(pierwszy);
    printf("\n");
    wypisz(drugi);
}

/// Zdanie Przepisanie z jednego do drugiego fragment
int main()
{
    int dlugosc(char* napis)
    {
        int i = 0;
        while(napis[i]!=0)
            i++;
        return i;
    }
    void przepisz(char*napis1,char*napis2,int n)
    {
        for(int i = 0;i<dlugosc(napis1)&& i<n;i++)
        {
            napis2[i]=napis1[i];
        }
        napis2[n]=0;
    }

    void wypisz(char*napis)
    {
        printf("%s",napis);
    }
    char*pierwszy = "arbuz";
    char drugi[20] = "arbiter";
    wypisz(pierwszy);
    printf("\n");
    wypisz(drugi);
    przepisz(pierwszy,drugi,3);
    printf("\n");
    wypisz(pierwszy);
    printf("\n");
    wypisz(drugi);
}

/// Zdanie sklejenie do drugiego
int main()
{
    void sklej(char*napis1,char*napis2,char*napis3)
    {
        int i,j;
        for(i=0;napis1[i]!=0;i++)
        {
            napis3[i]=napis1[i];
        }
        for(j=0;napis2[j]!=0;j++)
        {
            napis3[i]=napis2[j];
        }
    napis3[i]=0;
    }

    void wypisz(char*napis)
    {
        printf("%s",napis);
    }
    char*pierwszy = "alama";
    char *drugi = "kota";
    char trzeci[40];
    sklej(pierwszy,drugi,trzeci);
    printf(trzeci);
}

/// Zadanie male duze 
int main()
{
    void sklej(char*napis)
    {
        for(int i = 0; napis[i]!=0;i++)
        {
            if((napis[i]>='a')&&(napis[i]<='z'));
            {
                napis[i]=napis[i]+'A'-'a';
            }
        }
    }

   char napis[50] = "ten napis ma byc duzymi literami, a 2+2=4";
   sklej(napis);
   printf(napis);
}

/// Funkcja wyciac
int main()
{
   void funkcja(char* wyraz,int n, int z)
   {
       for(int i = 0;i<1; i++)
       {
           
           printf(wyraz);
       }
   }
   char* wyraz = "Informatyka";
   funkcja(wyraz);


}
