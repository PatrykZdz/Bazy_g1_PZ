# Cwiczenie 0.1
def funkcja(lista):
    list_no_repeat = set(lista)
    for x in list_no_repeat:
        print(x)

lista1 = [1,2,3,3,2,1]
funkcja(lista1)

# Cwiczenie 0.2
wyraz = "qwemewqawqemeqwa"
for x in range(len(wyraz)-1,2,-4):
    print(wyraz[x], end='')
print()
# Cwiczenie 0.3
def Fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))

def fib_i(n):
    if n == 0: return 0
    elif n == 1: return 1
    p, w = 0, 1
    for i in range(n-1):
        p, w = w, p+w
    return w

print(fib_i(10))

# Cwiczenie 0.4
def iloczyn_poteg(n, *args):
    iloczyn = 1
    for x in args:
        iloczyn *= x ** n
    return iloczyn

wynik = iloczyn_poteg(2, 1, 2, 3, 4, 5)
print(wynik)

# Cwiczenie 0.5
tab = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
tab2 = [len(x) for x in tab if 'u' in x or 'o' in x]
print(tab2)

tab = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']
tab2 = [len(word) for word in tab if 'u' in word or 'o' in word]
print(tab2)

def silnia(n):
    if (n==0 or n == 1):
        return 1
    else:
        return n*silnia(n-1)
def Newton(n,k):
    if k > n:
        return 0
    else:
        return silnia(n)/(silnia(k)*silnia(n-k))
print("Wynik = ",Newton(5,2))

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [0] * max(len(self.coefficients), len(other.coefficients))
        for i in range(len(result)):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] += other.coefficients[i]
        return Polynomial(result)

    def __sub__(self, other):
        result = [0] * max(len(self.coefficients), len(other.coefficients))
        for i in range(len(result)):
            if i < len(self.coefficients):
                result[i] += self.coefficients[i]
            if i < len(other.coefficients):
                result[i] -= other.coefficients[i]
        return Polynomial(result)

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        result = ''
        for i in range(len(self.coefficients)-1, -1, -1):
            if self.coefficients[i] != 0:
                if i == len(self.coefficients)-1:
                    result += f"{self.coefficients[i]}x^{i}"
                elif i == 0:
                    result += f" {'+' if self.coefficients[i] > 0 else '-'} {abs(self.coefficients[i])}"
                else:
                    result += f" {'+' if self.coefficients[i] > 0 else '-'} {abs(self.coefficients[i])}x^{i}"
        return result


p1 = Polynomial([2, 0, -1, 3]) # 2x^3 - x^2 + 3x + 2
p2 = Polynomial([1, -1, 1]) # x^2 - x + 1

print(p1) # 2x^3 - 1x^2 + 3x + 2
print(p2) # 1x^2 - 1x + 1

p3 = p1 + p2
print(p3) # 2x^3 + 0x^2 + 2x + 3

p4 = p1 - p2
print(p4) # 2x^3 - 2x^2 + 4x + 1

print(p1.degree()) # 3
print(p2.degree()) # 2
