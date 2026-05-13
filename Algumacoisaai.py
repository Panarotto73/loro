# HIHIHI TA FUNCIONANDOOO
# ===========================================
# |         CALCULADORA EM PYTHON           |
# |           Operações Básic               | 
# ===========================================


def soma(a, b):
    return a+b 

def subtracao(a, b):
    return a-b

def divisao(a, b):
    
    if b == 0:
        return "Div0"
    else:
        return a/b

def multip(a, b):
    return a*b


while True:
    print("=====Calculadora===== ")
    print("Soma: 1")
    print("Multiplicação: 2")
    print("Divisão: 3")
    print("Subtração: 4")
    print("Sair: 0 ")
   
    opcao = int(input("Escolha a operação:  "))

    if opcao == 0:
         break
  
    num1 = float(input("\nDigite o primeiro número: \n "))
    num2 = float(input("Digite o segundo número: \n"))

    if opcao == 1:

            resultado = soma(num1, num2)
            print(f"Resultado = {resultado}")

    elif opcao == 2:
        resultado = multip(num1, num2)
    print(f"Resultado = {resultado}")

    if opcao == 3:

            resultado = divisao(num1, num2)
            print(f"Resultado = {resultado}")

    if opcao == 1:

            resultado = subtracao(num1, num2)
            print(f"Resultado = {resultado}")


    break


#  FUNCINOU



