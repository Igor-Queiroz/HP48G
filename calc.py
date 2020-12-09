#variáveis
valores = []
vInt = False
quantDig = 0
operacoes = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão"]
operacao = 0
valorFinal = 0
lV = 0
lO = 0
operadorVal = False

#filtro de entrada (valor)
while vInt == False:
    quantDig = input("Quantos valores possui a operação?: ")

    if quantDig == "0" or quantDig == "1":
        print("Valor inválido. Insira um novo valor.")

    else:
        try: 
            int(quantDig)
            quantDig = int(quantDig)
            vInt = True

        except ValueError:
            try:
                float(quantDig)
                print("Valor inválido. Insira um novo valor.")

            except ValueError:
                print("Valor inválido. Insira um novo valor.")

#salva valores digitados no array
while lV < quantDig:
    valorN = input("Insira o " + str(lV + 1) + "° valor: ")

    try: 
        int(valorN)
        valores.append(int(valorN))
        lV+=1

    except ValueError:
        try:
            float(valorN)
            valores.append(float(valorN))
            lV+=1

        except ValueError:
            print("Valor inválido. Insira um novo valor.")

#mostra as operações
while lO < 4:
    print(operacoes.pop(0))
    lO+=1
    
#filtro de entrada (operação)
while operadorVal == False:
    operacao = input("Insira o valor da operação que deseja realizar: ")

    if operacao < "1" or operacao > "4":
        print("Valor inválido. Insira um novo valor.")

    else:
        try:
            int(operacao)
            operacao = int(operacao)
            operadorVal = True

        except ValueError:
            try:
                float(operacao)
                print("Valor inválido. Insira um novo valor.")

            except ValueError:
                print("Valor inválido. Insira um novo valor.")

#lógica do cálculo
def soma():
    while len(valores) > 1:
        calc = valores.pop() + valores.pop()
        valores.append(calc)
            
    if len(valores) == 1: print("Resultado: " + str(valores[0]))

#Não finalizado
#def subtracao():
    while len(valores) > 1:
        calc = valores.pop() - valores.pop()
        valores.append(calc)
            
    if len(valores) == 1: print("Resultado: " + str(valores[0]))

def multiplicacao():
    while len(valores) > 1:
        calc = valores.pop() * valores.pop()
        valores.append(calc)
            
    if len(valores) == 1: print("Resultado: " + str(valores[0]))

#Não finalizado
#def divisao():
    while len(valores) > 1:
        calc = valores.pop() / valores.pop()
        valores.append(calc)
            
    if len(valores) == 1: print("Resultado: " + str(valores[0]))


if operacao == 1:
    soma()

elif operacao == 2:
    #subtracao()
    print("Não definido")

elif operacao == 3:
    multiplicacao()

elif operacao == 4:
    #divisao()
    print("Não definido")