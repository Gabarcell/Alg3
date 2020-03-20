"""1. Faça um programa em Python que calcule o resultado da expressão abaixo. Os valores das
variáveis X, Y e Z podem ser constantes ou lidos pelo teclado.
X − 5 ∗ Y − Z
"""
import time

print('')
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
n = int(input("Digite o valor de z: "))

def tempo(): #tempo de espera
    time.sleep(3)

def show():   #processamento do calculo
    print('---------------------------------')
    print("          Processando...")
    print('---------------------------------')
    tempo()

def soma(x,y,n): #soma com parênteses
    som = (x-5)*(y-n)
    return som

def sum(x,y,n): #soma sem parênteses
    so = x-5*y-n
    return so

def result():    #mostra resultados
    print("Resultado 01: ", soma(x, y, n))
    print("Resultado 02: ", sum(x, y, n))
    print('---------------------------------')

show()
result()


