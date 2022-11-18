select * from postac;
#lab 4, zadanie 1 a)

select * from postac 
where nazwa != 'Bjorn' and rodzaj = 'wiking'
order by data_ur ASC
limit 2;
delete from postac 
where id_postaci = 6;

#lab 4, zadanie 1b
alter table postac drop primary key; 
# problem 1 - istniejące klucze obce do tej kolumny;
#tabela przetwory, walizka , ewuentualnie izba
#usuwanie kluczy obcych;
alter table przetwory drop foreign key przetwory_ibfk_1;
# aby sprawdzic nazwy kluczy obcych
show create table przetwory;
#problem 2 - atrybut auto_increment 
alter table postac modify id_postaci int;
#drop primary key powinien zadziałać
alter table postac drop primary key;
#lab 4 zadanie 2a
# first - wstawiamy kolumnę jako pierwszą w tabeli 
alter table postac add pesel char (11) first;
alter table postac add primary key (pesel);
update postac set pesel=0;
select * from postac;
update postac set pesel = '74645342541' + id_postaci;
#lab 4 zadanie 2b
alter table postac modify rodzaj enum('syrena');
#lab 4 zadanie 2c
alter table

# lab 4 zadanie 3a
update postac set statek = 'Statek Bjorna' 
where nazwa like '%a%';

# lab 4 zadanie 3b
update statek set max_ladownosc=max_ladownosc*0.7
where data_wodowania >= '1901-01-01'
and data_wodowanie <= '2000-12-31';
#lub
# where year (select year(data_ur) from statek; )







