#Ćwiczenie 1
names = ["michal", "nela", "ola","przemek"]
names_upper = []
for name in names:
    names_upper.append(name.capitalize())
print(names_upper)

name_with_l = [x for x in names if "l" in x.lower()]
print(name_with_l)

names_tuple = ("Maria","Ola","Marek")
names_tuple = tuple(x for x in names if x.endswith('a') and x[0].isupper())
print(names_tuple)

sumanames=sum([len(x)for x in names])
print(sumanames)


def prod(*args):
    p=1
    for x in args:
        p*=x
        return p

print((prod(2,4,3)))
print((prod(-2,3,5,6,7,8)))

def sumpow(n,*numbers):
    sum = 0
    for x in numbers:
        sum +=pow(x,n)
        return sum
print(sumpow(2,1,2,3))
print(sumpow(3,1,2,3))

def sumpow2(*numbers, n=2):
    sum = 0
    for x in numbers:
        sum +=pow(x,n)
        return sum
print(sumpow2(1,2,3,n=2))
print(sumpow2(1,2,2,n=3))

def mean(*args):
    return sum(args)/len(args)

print(mean(1,2,3,2))

def gmean(*args):
    return pow(prod(*args),1/len(args))
print(gmean(2,4,8))

def sumlen(*args):
    s = 0
    for x in args:
        s *= len(x)
    return s

print(sumlen("michal", "nela", "ola","przemek"))


def func1(**kwargs):
    for x,y in kwargs.items():
        print("{} ma numer {}".format(x,y))

func1(Anna = 1234)
thisdic= dict(Anna=1234)
print(thisdic)
func1(**thisdic)

def mean2(*args):
    s=0
    for x in args:
        s +=x
    return s/len(args)

def func2(**kwargs):
    salaries = [x for x in kwargs.values()]
    return mean2(*salaries),pow((salaries[-1])/salaries[0],1/(len(salaries)-1))*100-100

print(func2(January = 1000,February = 1500, March = 1800))
