"""
3. Faça um programa em Python que receba (leitura do teclado) 3 notas e seus respectivos
pesos, calcule e mostre a média ponderada dessas notas.
Média Ponderada =
(Nota 1 ∗ Peso da Nota 1)+ (Nota 2 ∗ Peso da Nota 2)
-----------------------------------------------------
              Soma dos Pesos das Notas
"""


import time

def tempo():
    time.sleep(3)
def ask():
    print("")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    p1 = 10
    p2 = 10
    s = p1+p2
    if n1 and n2 <= p1: #verifica se nota é menor ou igual ao peso
        media = ((n1 * p1) + (n2 * p2)) / s     #calculo da expressao

        print('---------------------------------')
        print("          Processando...")
        print('---------------------------------')
        tempo()

        return print(f"Sua média é: {media:.2f}")
    return print("A nota do aluno tem que ser menor ou igual peso da nota")
ask()

