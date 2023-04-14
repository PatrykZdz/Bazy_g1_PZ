#Ćwicznie 1
class Fruit:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return str("color "+str(self.color)+"\n weight:"+str(self.weight))
    def __add__(self,other):
        return Fruit(' ',self.weight+other.weight)
class Apple(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "red" or self.color == "green"):
            return True
        else:
            return False
class Banan(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "yellow"):
            return True
        else:
            return False
class Orange(Fruit):
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def isfresh(self):
        if(self.color == "orange"):
            return True
        else:
            return False
my_fruit=Banan("yellow,",350)
my_fruit2=Fruit("pomaranczowe",250)
print(my_fruit+my_fruit2)
print(my_fruit.isfresh())
#Ćwiczenie 2
class Account:
    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if (amount > self.balance):
            print("Brak srodkow")
        else:
            self.balance -= amount
    def transfer(self,amount,to_account):
        if amount > self.balance:
            print("Brak srodkow")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)
class PrivatAccount(Account):
    def __init__(self,account_number,balance = 0,salary = 0):
        self.account_number=account_number
        self.balance=balance
        self.salary = salary
    def pay_salary(self):
        self.deposit(self.salary)
class FirmAccount(Account):
    def Przelewy(self,transfer_to_ZUS,transfer_to_US):
        self.transfer_to_ZUS=transfer_to_ZUS
        self.transfer_to_US=transfer_to_US
#Ćwiczenie 3
class Romanian:
    def Na_Rzymskie(self,wartosc):
        wartosci = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbole = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        rzymska_liczba = ""
        i = 0
        while wartosc> 0:
            for _ in range(wartosc//wartosci[i]):
                rzymska_liczba +=symbole[i]
                wartosc -= wartosci[i]
            i+=1
        return rzymska_liczba
    def Na_Arabskie(self, roman_numeral):
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_numeral = 0
        previous_value = 0
        i = len(roman_numeral) - 1
        while i >= 0:
            current_value = self.roman_dict[roman_numeral[i]]
            if current_value >= previous_value:
                arabic_numeral += current_value
            else:
                arabic_numeral -= current_value
            previous_value = current_value
            i -= 1
        return arabic_numeral
    def dodowanie(self,other):
        return Romanian(self.Na_Arabskie()+other.to_Na_Arabskie().to_Na_Rzymskie)
print(Romanian().Na_Rzymskie(549))
print(Romanian().Na_Arabskie("DXLIX"))
