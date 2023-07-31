def soma(b, c):
    resposta = 0
    a = b + c
    resposta = a
    return resposta

def subtracao(b, c):
    resposta = 0
    a = b - c
    resposta = a
    return resposta

def multiplicacao(b, c):
    resposta = 0
    a = b * c
    resposta = a
    return resposta

def divisao(b, c):
    resposta = 0
    a = b / c
    resposta = a
    return resposta

def potencia(b, c):
    resposta = 0
    a = b ** c
    resposta = a
    return resposta

num_operacoes = int(input())

if num_operacoes > 0:
    for i in range(1, num_operacoes + 1):
        operacao = input()
        operando_1 = float(input())
        operando_2 = float(input())

        if operacao == "Quero somar esses dois números:":
            resultado = soma(operando_1, operando_2)
        elif operacao == "Preciso subtrair um pelo outro":
            resultado = subtracao(operando_1, operando_2)
        elif operacao == "Quanto dá o produto disso?":
            resultado = multiplicacao(operando_1, operando_2)
        elif operacao == "Vou dividir aqui rapidinho":
            resultado = divisao(operando_1, operando_2)
        elif operacao == "E se eu elevar um pelo outro?":
            resultado = float(potencia(operando_1, operando_2))

        print(f"O resultado da {i}ª operação foi {resultado:.1f}")

        i += 1

    print("Ufa, já deu de cálculos por hoje!")
else:
    print("Vou relaxar aqui na minha nave")