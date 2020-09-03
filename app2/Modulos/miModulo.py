from functools import reduce
def Exp(x, n):
        if n == 0:
            return 1
        return x * Exp(x, n - 1)

def ShowMessage(message):

        print (f"{message}")



data = str(17262)


def CalcularCifras(data):
    r = reduce(lambda x , y : int(x) + int(y), data)
    return r

r = CalcularCifras(data)

ShowMessage(r)

