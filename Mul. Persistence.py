import random

def Per(n):
    original = n
    t = 0
    while n>10:
        singlen = [int(d) for d in str(n)]
        resultado = 1
        for number in singlen:
            if number != 0:
                resultado *= number
        n = resultado
        t += 1
    return [original,t]


def Tester(n):
    a = str(2)
    b = str(3)
    c = str(7)
    d = str(5)
    number = 1

    while True:
        if Per(number)[1] >= n:
            return [number, Per(number)[1]]
        else:
            number = str((a*random.randint(0,100000))+(b*random.randint(0,100000))+(c*random.randint(0,100000))+(d*random.randint(0,100000)))
            if number == "":
                number = 0
            else:
                number = int(number)

print(Tester(15))
