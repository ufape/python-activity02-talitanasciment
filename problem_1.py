# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Digite 6 valores inteiros quaisquer.
Exemplo:
Digite o valor 1/6: 2
Digite o valor 2/6: 3
Digite o valor 3/6: 4
Digite o valor 4/6: 5
Digite o valor 5/6: 6
Digite o valor 6/6: 7

Processes:
Faça um programa que leia 6 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Output(s):
Exemplo:
Você digitou 3 valores pares.
"""


def main():
   a = int(input(f"Digite o valor A: "))
   b = int(input(f"Digite o valor B: "))
   c = int(input(f"Digite o valor C: "))
   d = int(input(f"Digite o valor D: "))

   if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a %2 == 0:
     print("Valores aceitos.")
   else:
     print("Valores recusados.")
if __name__ == '__main__':
    main()
