valor=float(input("Digite o valor em reais que deseja cambiar:"))
print("Digite (1) para dólar.\nDigite (2) para Euro.\nDigite (3) para Libra Esterlina.\nDigite (4) para Iene.\nDigite (5) para Dolar Australiano.")


def opcao1():
    print("\nVocê escolheu Dolar")
    conversao=valor/5.12
    print(round (conversao, 2))

def opcao2():
    print("\nVocê escolheu Euro")
    conversao=valor/5.49
    print(round (conversao, 2))

def opcao3():
    print("\nVocê escolheu Libra Esterlina")
    conversao=valor/6.43
    print(round (conversao, 2))

def opcao4():
    print("\nVocê escolheu Iene")
    conversao=valor/0.033
    print(round (conversao, 2))

def opcao5():
    print("\nVocê escolheu Dolar Australiano")
    conversao=valor/3.36
    print(round (conversao, 2))

def opcao_padrao():
    print("Opção inválida")

opcoes = {
    1: opcao1,
    2: opcao2,
    3: opcao3,
    4: opcao4,
    5: opcao5,
}

def switch_case(opcao):
    funcao = opcoes.get(opcao, opcao_padrao)
    funcao()

opcao = int(input("\nEscolha uma opção:\n"))

switch_case(opcao)

