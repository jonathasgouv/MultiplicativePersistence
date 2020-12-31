import random

factor = 50000

def Per(n):
    original = n
    t = 0
    while n>10:
        singlen = [int(d) for d in str(n)]
        resultado = 1
        for number in singlen:
            resultado *= number
        n = resultado
        t += 1
    return [original,t]


def Tester(n):
    a = str(2)
    b = str(3)
    c = str(7)
    number = 1
    while True:
        if Per(number)[1] > n:
            return number, Per(number)[1]
        else:
            number = str((a*random.randint(0,factor))+(b*random.randint(0,factor))+(c*random.randint(0,factor)))
            if number == "":
                number = 0
            else:
                number = int(number)


#print(Tester(3))
#print(Per(5555555))
