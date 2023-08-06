#!/usr/bin/python3
import math
import sys

def circulo(raio):
    return math.pi * raio ** 2

# Função que informa quando dá algum erro
def help():
    print("""\
    É necessário informar o raio do círculo.
    Sintaxe: area_circulo <raio>""")

if __name__ == '__main__':

    # O sys.argv recebe os parâmetros passados pela linha de comando
    # O argv[0] é sempre o nome do script (area_circulo)
    if len(sys.argv) < 2:
        help()

        # Retorna sempre diferente de 0 em caso de erro
        # Dessa forma, nem precisa do else
        sys.exit(1)

    if not sys.argv[1].isnumeric():
        help()
        print("O raio deve ser um valor inteiro!")
        sys.exit(2)

    raio = int(sys.argv[1])
    area = circulo(raio)
    print('Área do círculo', area)