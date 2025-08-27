import random
import numpy as np
import math

def credito():
     
    saldo_str = input("coloque")
    saldo_int = int(saldo_str)
    if saldo_int % 2 != 0:
        print("Só aceitamos valores pares")
        credito()
    return saldo_int
    

def randomico():
    
    saldo = credito()
    qtdJogada = saldo/2
    text = "{:.1f}".format(qtdJogada)
    if text.endswith(".0"):
        text = text[:-2]
    print("User credits ", text)
    
    while qtdJogada > 0: 
        ranvet = []
        for i in range(0,9):
            rans = random.randrange(0, 9)
            ranvet.append(rans)
        matriznumpy = np.array(ranvet).reshape(3, 3)
    return matriznumpy
    print("cabo")

ran = randomico()
print(ran)

if ran[1][0] == ran[1][1] == ran[1][2]:
    print("ganho")

if ran[0][2] == ran[1][1] == ran[2][0]:
    print("ganhoU")

if ran[0][0] == ran[1][1] == ran[2][2]:
    print("bonus22")