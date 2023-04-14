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
    def __init__(self,color):
        self.color = color
    def isfresh(self):
        if(self.color == "red" or self.color == "green"):
            return True
        else:
            return False
class Banan(Fruit):
    def __init__(self,color):
        self.color = color
    def isfresh(self):
        if(self.color == "yellow"):
            return True
        else:
            return False
class Orange(Fruit):
    def __init__(self,color):
        self.color = color
    def isfresh(self):
        if(self.color == "orange"):
            return True
        else:
            return False

my_fruit=Fruit("czerwony,",350)
my_fruit2=Fruit("pomaranczowe",250)
print(my_fruit+my_fruit2)


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
    def __init__(self,account_number,balance = 0):
        self.account_number=account_number
        self.balance=balance




class RomanToArabic:
    def __init__(self):
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_to_arabic(self, roman_numeral):
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

