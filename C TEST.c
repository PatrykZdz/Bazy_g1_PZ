
Napisz funkcję find_max_pointed_numbers, która ma dwa argumenty. Pierwszym argumentem
jest wskaźnik num1 na stałą wartość typu double, a drugim argumentem jest stały wskaźnik
num2 na zmienną typu double. Funkcja find_max_pointed_numbers ma zwrócić liczbę
zawierającą większą wartość spośród wartości wskazywanych przez pierwszy i drugi wskaźnik.
Stwórz przypadek testowy dla funkcji.

Przykładowa sytuacja przed wywołaniem funkcji:
Nazwa zmiennej Wartość zmiennej Adres zmiennej
a 4.2 0x00204
b -3.4 0x00338
Funkcja ma zwrócić dla powyższych danych 4.2.

#include <stdio.h>
#include <stdlib.h>

double find_max_pointed_numbers(const double *num1, const double *num2)
{
    if(*num1 > *num2)
        return *num1;
    return *num2;

}

int main()
{
    double a = 4.2;
    double b = -3.4;
    printf("%.1f",find_max_pointed_numbers(&a,&b));
    return 0;
}


Napisz rekurencyjną funkcję sequence_value_d, która dla otrzymanej w argumencie nieujemnej
liczby całkowitej 𝑛 zwraca wartość elementu o indeksie 𝑛 ciągu zdefiniowanego w następujący
sposób:
𝑑0 = 3
𝑑𝑛 = 𝑑𝑛−1 − 3, 𝑛-parzyste,
𝑑𝑛 = 2 ⋅ 𝑑𝑛−1 + 4, 𝑛-nieparzyste.


#include <stdio.h>
#include <stdlib.h>

int sequence_value_d(unsigned int n)
{
    if(n==0)
        return 3;
    else if (n%2 ==0)
        return sequence_value_d(n-1)-3;
    return 2*sequence_value_d(n-1)+4;

}


int main()
{
    printf("%d\n",sequence_value_d(5));
    printf("%d",sequence_value_d(3));
    return 0;
}


Napisz funkcję, która otrzymuje cztery argumenty: dodatnią liczbę całkowitą n, n-elementowe
tablice tab1 i tab2 oraz n-elementową tablicę tab3 o elementach typu double. Funkcja powinna
obliczać iloczyn elementów tablic tab1 i tab2 o tych samych indeksach i zapisywać wyniki do
tablicy tab3. Stwórz przypadek testowy dla funkcji.


#include <stdio.h>
#include <stdlib.h>

void funkcja(int n,double tab1[n],double tab2[n],double tab3[n])
{
    for(int i=0;i<n;i++)
    {
       tab3[i] = tab1[i]*tab2[i];
    }
}

void wypisz(int n,double tab[])
{
    for(int i=0;i < n;i++)
    {
        printf("%.2f ",tab[i]);
    }
    printf("\n");
}


int main()
{
    double tab1[] = {2.0,4.0,6.0};
    double tab2[] = {3.0,5.0,7.0};
    int n =3;
    double tab3[] = {};
    funkcja(n,tab1,tab2,tab3);

    wypisz(n,tab1);
    wypisz(n,tab2);
    wypisz(n,tab3);


    return 0;
}


Napisz funkcję linear_function_value, która ma trzy argumenty. Pierwszym argumentem jest wskaźnik a na stałą wartość typu float, drugim argumentem jest stały wskaźnik b na zmienną typu float, a trzecim argumentem jest wskaźnik x na stałą wartość typu float. Funkcja linear_function_value ma zwrócić wartość funkcji liniowej o współczynnikach wskazywanych przez wskaźniki a i b dla argumentu x (y=ax+b). Stwórz przypadek testowy dla funkcji.


#include <stdio.h>
#include <stdlib.h>

double linear_function_value(const float *a,const float *b, const float *x)
{
    return (*a)*(*x)+(*b);
}

int main()
{
    float a = 1.0;
    float b = 2.0;
    float x = 3.0;
    printf("%f", linear_function_value(&a,&b,&x));
    return 0;
}


Napisz rekurencyjną funkcję sum_of_digits, która zwraca sumę cyfr otrzymanej w argumencie nieujemnej liczby całkowitej 𝑛. Stwórz dwa przypadki testowe.


#include <stdio.h>
#include <stdlib.h>

int sum_of_digits(int n)
{
    if (n == 0) {
        return 0;
    }
    return sum_of_digits(n/10) + (n%10);
}


int main()
{
    printf("%d",sum_of_digits(234));
    return 0;
}





Napisz bezargumentową funkcję init_block, która rezerwuje blok czterech zmiennych typu float. Funkcja ma ustawić kolejno w pamięci wartości 0.5, 1.5, 2.5 i 3.5. Na koniec funkcja powinna zwrócić wskaźnik na początkową zmienną z bloku. Stwórz przypadek testowy w main tak, aby wyświetlić na konsoli wartości zmiennych przechowywanych na bloku stworzonym wewnątrz funkcji. 

#include <stdio.h>
#include <stdlib.h>

float* init_block() {
    float* block = (float*)malloc(4 * sizeof(float));
    if (block == NULL) {
        printf("Błąd alokacji pamięci\n");
        exit(EXIT_FAILURE);
    }

    *block = 0.5;
    *(block + 1) = 1.5;
    *(block + 2) = 2.5;
    *(block + 3) = 3.5;

    return block;
}

int main() {
    float* block_start = init_block();

    // Wyświetlanie wartości zmiennych przechowywanych na bloku
    for (int i = 0; i < 4; i++) {
        printf("Wartość zmiennej %d: %.1f\n", i+1, *(block_start + i));
    }

    free(block_start); // Zwolnienie pamięci zaalokowanej dla bloku

    return 0;
}



Napisz rekurencyjną funkcję polynomial_value, która zwraca wartość wielomianu dla otrzymanej w argumencie nieujemnej liczby całkowitej 𝑛 oraz wartości x, gdzie wielomian jest zdefiniowany w następujący sposób: 𝑝0(𝑥) = 1 𝑝𝑛+1(𝑥) = (𝑥−1)𝑝𝑛(𝑥)+1,𝑛 ⩾ 0 Funkcja powinna przyjmować dwa argumenty: nieujemną liczbę całkowitą n oraz wartość rzeczywistą x. Stwórz dwa przypadki testowe.


#include <stdio.h>

double polynomial_value(int n, double x) {
    // Warunek bazowy
    if (n == 0) {
        return 1;
    }
    // Wywołanie rekurencyjne
    return (x - 1) * polynomial_value(n - 1, x) + 1;
}

int main() {
    // Przypadki testowe
    int n1 = 3;
    double x1 = 2.0;

    int n2 = 4;
    double x2 = 3.0;

    // Wyświetlenie wartości wielomianu dla obu przypadków testowych
    printf("Wartość wielomianu dla n=%d, x=%.1f: %.2f\n", n1, x1, polynomial_value(n1, x1));
    printf("Wartość wielomianu dla n=%d, x=%.1f: %.2f\n", n2, x2, polynomial_value(n2, x2));

    return 0;
}
