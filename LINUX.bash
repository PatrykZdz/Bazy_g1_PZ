Zad 1
#!/bin/bash

las=false
a1=false

for param in "$@"; do
    if [ "$param" = "las" ]; then
        las=true
    elif [ "$param" = "a1" ]; then
        a1=true
    fi
done

if [ "$las" = true ]; then
    echo "Wczytano wartość 'las'"
fi

if [ "$a1" = true ]; then
    echo "Wczytano wartość 'a1'"
    echo "Liczba zwykłych plików w katalogu domowym: $(find ~/ -maxdepth 1 -type f | wc -l)"
fi



Zad 2
#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo "Za malo"
    exit 11
elif [ "$#" -eq 3 ]; then
    touch "$2"
    ls -l ~ > "$2"
    exit 55
else
    echo "Liczba podkatalogów do 3 poziomu zagłębienia: $(find . -mindepth 1 -maxdepth 3 -type d | wc -l)"
    exit 22
fi

Zad 3
#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Podaj nazwę pliku do sprawdzenia"
    exit 1
fi

filename="$1"

if [ -e "$filename" ]; then
    echo "Pliki o rozmiarze większym niż 150B w katalogu bieżącym:"
    find . -type f -size +150c -exec basename {} \;
else
    echo "Plik $filename nie istnieje w katalogu bieżącym"
fi


Zad 4
#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Za mało parametrów"
    exit 1
fi

first_param="$1"
count=0

shift

for param in "$@"; do
    if [ "$param" = "$first_param" ]; then
        ((count++))
    fi
done

echo "Liczba powtórzeń pierwszego parametru: $count"

Zad 5
#!/bin/bash

script_name=$(basename "$0")
read -p "Podaj nazwę: " input

if [ "$input" = "$script_name" ]; then
    echo "Wczytana wartość jest równa nazwie uruchomionego skryptu."
else
    echo "Wczytana wartość nie jest równa nazwie uruchomionego skryptu."
fi

Zad 6
#!/bin/bash

if [ "$#" -gt 3 ]; then
    echo "Za dużo parametrów"
    exit 1
elif [ "$#" -le 3 ]; then
    echo "Ilość parametrów: $#"
fi

if [ "$#" -gt 3 ]; then
    echo "Pierwszy parametr: $1"
    echo "Trzeci parametr: $3"
    if [ "$1" = "$3" ]; then
        echo "Pierwszy i trzeci parametr są sobie równe."
    else
        echo "Pierwszy i trzeci parametr nie są sobie równe."
    fi
    exit 0
fi

exit 17


Zad 7
#!/bin/bash

if [ "$#" -gt 4 ]; then
    echo "Za dużo parametrów"
    exit 25
elif [ "$#" -eq 1 ]; then
    if [ "$1" = "drzewo" ]; then
        tree
    elif [ "$1" = "zwykle" ]; then
        echo "Pliki zwykłe w katalogu bieżącym:"
        find . -type f -printf "%f\n"
    else
        echo "Numer procesu: $$"
        exit 123
    fi
else
    echo "Numer procesu: $$"
    exit 123
fi

Zad 8
#!/bin/bash

echo "Katalog domowy użytkownika: $HOME"
echo "Liczba użytkowników zalogowanych: $(who | wc -l)"

Zad 9
#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Za mało parametrów"
    exit 1
fi

first_param="$1"

if [ "$first_param" = "dwa" ]; then
    echo "Dzisiejsza data: $(date +"%Y-%m-%d")"
    exit 0
elif [ "$#" -eq 2 ]; then
    second_param="$2"
    if [ -f "$second_param" ]; then
        echo "Plik $second_param istnieje w bieżącym katalogu."
        exit 0
    else
        echo "Plik $second_param nie istnieje w bieżącym katalogu."
        exit 1
    fi
fi

exit 0

Zad 10
#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Za mało parametrów"
    exit 1
fi

first_param="$1"
second_param="$2"

if [ "$second_param" = "tworz" ]; then
    read -p "Podaj nazwę pliku: " filename
    echo "PID: $$" >> "$filename"
    echo "PID został dodany do pliku $filename"
    exit 0
fi



