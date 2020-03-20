"""
2. Faça um programa em Python que receba dois valores fornecidos pelo usuário, efetue a
troca destes valores e apresente os valores trocados. Baseie-se no exemplo de execução
abaixo, mas lembre-se que é apenas um exemplo. Os valores fornecidos por um usuário
qualquer podem ser diferentes dos fornecidos.
"""

import time
print('')
a = int(input("Digite Variavel 1: "))
b = int(input("Digite Variavel 2: "))

def tempo():
    time.sleep(3)

def show():         #mostra valores input
    print('---------------------------------')
    print("Valor 1:",a,"\nValor 2:", b)
    print('---------------------------------')
    return print("Invertendo, aguarde!")

def inverter(a,b):   #armazena e inverte as variaveis
    aux = b
    b = a
    a = aux
    return print("Valor 1: ",a,"\nValor 2: ",b)

show()
print('---------------------------------')
tempo()
print(inverter(a,b))
