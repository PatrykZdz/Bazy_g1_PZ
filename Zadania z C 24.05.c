#include <stdio.h>
struct element
{
    int i;
    struct element*next;
};
struct element* utworz()
{
    return NULL;
};
void wyczysc(struct element* Lista)
{
    struct element *wsk =Lista;
    while (Lista!=NULL)
    {
        Lista = Lista->next;
        free(wsk);
        wsk=Lista;
    }
}
struct element*dodajnapoczatek(struct element* Lista,int a)
{
    struct element*wsk=malloc(sizeof(struct element));
    wsk->i=a;
    wsk->next=Lista;
    return wsk;
};
struct element*nakoniec(struct element* Lista,int a)
{
    struct element *wsk;
    if(Lista==NULL)
    {
        Lista=wsk=malloc(sizeof(struct element));
    }
    else
    {
        wsk=Lista;
    while(wsk->next!=NULL)
    {
        wsk=wsk->next;
    }
    wsk->next=malloc(sizeof(struct element));
    wsk=wsk->next;
    }
    wsk->i=a;
    wsk->next=NULL;
    return Lista;
};
int dlugosc(struct element *Lista)
{
    int sum=0;
    while(Lista!=NULL)
    {
        sum=sum+1;
        Lista=Lista->next;
    }
    return sum;
}
int suma(struct element*Lista)
{
    int suma2 = 0;
    while(Lista!=NULL)
    {
        suma2=suma2+Lista->i;
        Lista=Lista->next;
    }
    return suma2;
}
void wypisz(struct element*Lista)
{
    while(Lista!=NULL)
    {
        printf("%d\n",Lista->i);
        Lista=Lista->next;
    }
    printf("\n");
}
int min(struct element*Lista)
{
    int min=Lista->i;
    while(Lista!=NULL)
    {
        if(Lista->i<min)
        {
            min=Lista->i;
        }
        Lista=Lista->next;
    }
}
struct element*dodaj_odpowiednio(struct element* Lista,struct element*elem, int a)
{
    struct element *wsk=malloc(sizeof(struct element));
    wsk->i=a;
    if(elem==NULL)
    {
        wsk->next=Lista;
        Lista=wsk;
    }
    else
    {
        wsk->next=elem->next;
        elem->next=wsk;
    }
    return Lista;

};
struct element*usun(struct element* Lista,int a)
{
    struct element*wsk,*wsk2;
    if(Lista==NULL)
    {
        return Lista;
    }
    wsk=Lista;
    if(Lista->i==a)
    {
        Lista=Lista->next;
        free(wsk);
    }
    else
    {
        while((wsk->next!=NULL)&&(wsk->next->i!=a))
        {
            wsk=wsk->next;
        }
        if(wsk->next!=NULL)
        {
            wsk2=wsk->next;
            wsk->next=wsk2->next;
            free(wsk2);
        }
    }
    return Lista;
};
int main()
{
    struct element *lista=utworz();
    lista =nakoniec(lista,4);
    wypisz(lista);
    lista =nakoniec(lista,15);
    wypisz(lista);
    lista =nakoniec(lista,3);
    wypisz(lista);
    lista =nakoniec(lista,-7);
    wypisz(lista);
    lista =nakoniec(lista,9);
    wypisz(lista);
    lista =nakoniec(lista,-2);
    wypisz(lista);
    lista=dodajnapoczatek(lista,6);
    wypisz(lista);
}


