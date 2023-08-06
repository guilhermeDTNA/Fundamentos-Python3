#!/usr/bin/python3

def fibonnaci(limite):
    resultado = [0, 1]

    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])

        if len(resultado) == limite-1:
            # O break pode ser usado para o while e para o for
            break
        
    return resultado


def gerandoNumeros(max):
    resultado = []
    
    # Gera os números entre 2 e o máximo-1 de forma ordenada
    for i in range(2, max):
        resultado.append(i)

    print("Lista gerada: ", resultado)

if __name__ == '__main__':
    for fib in fibonnaci(1000):
        print(fib)

    gerandoNumeros(20)    