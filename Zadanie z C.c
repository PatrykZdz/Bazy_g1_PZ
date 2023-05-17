https://github.com/kinja/programowanie-C/tree/master/Zadania%20z%20programowania%20w%20jezyku%20C%20C%2B%2B%2C%20cz.%20I%20-%20Jacek%20Krzaczkowski

#include <stdio.h>
#include <math.h>
struct trojkat
{
    double a,b,c;
};
double obwod(struct trojkat t)
{
    return t.a+t.b+t.c;
}
double pole (struct trojkat t)
{
    double p  = (t.a+t.b+t.c)/2;
    return sqrt(p*(p-t.a)*(p-t.b)*(p-t.c));
}
void komunikat_czy_da_zbudowac(struct trojkat t)
{
    if(t.a+t.b<t.c)
    {
       printf("Nie da sie zbudowac");
    }
}

void jaki_trojkat(struct trojkat t)
{
    if(pow(t.a,2)+pow(t.b,2)<pow(t.c,2))
    {
        printf("Trojkat ostrokatny");
    }
    else if(pow(t.a,2)+pow(t.b,2)==pow(t.c,2))
    {
        printf("Trojkat prostokatny");
    }
    else
    {
        printf("Trojkat rozwartokatny");
    }

}
int main()
{
    struct trojkat t1;
    t1.a = 3;
    t1.b = 4;
    t1.c = 2;
    printf("%f\n",obwod(t1));
    printf("%d\n",sizeof(double));
    printf("%d\n",sizeof(struct trojkat));
    printf("Pole wynosi = %f\n",pole(t1));
    komunikat_czy_da_zbudowac(t1);
    jaki_trojkat(t1);
}

void jaki_trojkat(struct trojkat t)
{
    if(pow(t.a,2)+pow(t.b,2)<pow(t.c,2))
    {
        printf("Trojkat ostrokatny");
    }
    else if(pow(t.a,2)+pow(t.b,2)==pow(t.c,2))
    {
        printf("Trojkat prostokatny");
    }
    else if(pow(t.a,2)+pow(t.b,2)>pow(t.c,2))
    {
        printf("Trojkat rozwartokatny");
    }
///zle
}

#include <stdio.h>
#include <math.h>
struct trojkat
{
    double a,b,c;
};
void przepisz(struct trojkat t1, struct trojkat *t2)
{
    *t2=t1;
}
void wypisz(struct trojkat tr1)
{
    printf("%f\n",tr1.a);
    printf("%f\n",tr1.b);
    printf("%f\n",tr1.c);
    printf("\n");
}
int main()
{
    struct trojkat t1;
    t1.a = 3;
    t1.b = 4;
    t1.c = 5;
    struct trojkat t2;
    t2.a = 1;
    t2.b = 1;
    t2.c = 1;
    struct trojkat *wsk2=&t2;
    wypisz(t1);

    wypisz(t2);
    przepisz(t1,wsk2);
    printf("Po zmianie\n");
    wypisz(t1);
    wypisz(*wsk2);
}

#include <stdio.h>
struct punkt
{
    double x,y,z;
};
double odleglosc(struct punkt P,struct punkt R)
{
    return sqrt(pow(P.x-R.x,2)+pow(P.y-R.y,2)+pow(P.z-R.z,2));
}
double minimum(struct punkt tab[], int n)
{
    int i,j;
    double pom;
    double min = odleglosc(tab[0],tab[1]);
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            pom = odleglosc(tab[i],tab[j]);
        }
        if(pom<min)
        {
            min=pom;
        }
    }
    return min;
}
int main()
{
    struct punkt P;
    P.x=1;
    P.y =7;
    P.z =2;
    struct punkt Q;
    Q.x = 4;
    Q.y = 9;
    Q.z = 0;
    struct punkt R;
    R.x=2;
    R.y=5;
    R.z=8;
    struct punkt tab[3]= {P,Q,R};
    printf("%f",minimum(tab,3));
}

#include <stdio.h>
struct zespolone
{
    double a,b;
};
void wyswietl_liczbe_zespolona(struct zespolone liczba)
{
    printf("%f + %f i\n",liczba.a,liczba.b);
}
void wczytaj_liczbe_zespolona(struct zespolone liczba)
{
    scanf("%lf",&liczba.a);
    scanf("%lf",&liczba.b);
}
struct zespolone dodaj(struct zespolone liczba1, struct zespolone liczba2)
{
    struct zespolone suma;
    suma.a =liczba1.a+liczba2.a;
    suma.b =liczba1.b+liczba2.b;
    return suma;
};
struct zespolone iloczyn(struct zespolone liczba1, struct zespolone liczb2)
{
    struct zespolone wynik;
};
int main()
{
    struct punkt P;
    P.x=1;
    P.y =7;
    P.z =2;
    struct punkt Q;
    Q.x = 14;
    Q.y = 9;
    Q.z = 0;
    struct punkt R;
    R.x=2;
    R.y=5;
    R.z=8;
    struct punkt tab[3]= {P,Q,R};
    printf("%f",minimum(tab,3));
}

#include <stdio.h>
struct zespolone
{
    double a,b;
};
void wyswietl_liczbe_zespolona(struct zespolone liczba)
{
    printf("%f + %f i\n",liczba.a,liczba.b);
}
void wczytaj_liczbe_zespolona(struct zespolone liczba)
{
    scanf("%lf",&liczba.a);
    scanf("%lf",&liczba.b);
}
struct zespolone dodaj(struct zespolone liczba1, struct zespolone liczba2)
{
    struct zespolone suma;
    suma.a =liczba1.a+liczba2.a;
    suma.b =liczba1.b+liczba2.b;
    return suma;
};
double modul_liczby_zespolonej(struct zespolone liczba)
{
    return pow((liczba.a*liczba.a+liczba.b*liczba.b),0.5);
}
int main()
{
    struct zespolone X;
    X.a=2;
    X.b=7;
    wyswietl_liczbe_zespolona(X);
    printf("Modul liczby zespolonej wynosi %f\n",modul_liczby_zespolonej(X));
}

#include <stdio.h>
union super_int{
    int i;
    unsigned int n;
};
struct wiele_int
{
    int i;
    unsigned int n;
};
int main()
{
    struct wiele_int X;
    union super_int Y;
    printf("%d\n",sizeof(int));
    printf("%d\n",sizeof(unsigned int));
    ///Struktura
    printf("%d\n",sizeof(X));
    printf("%p\n",&X);
    printf("%p\n",&X.i);
    printf("%p\n",&X.n);
    ///Unia
    printf("%d\n",sizeof(Y));
    printf("%p\n",&Y);
    printf("%p\n",&Y.i);
    printf("%p\n",&Y.n);
}



