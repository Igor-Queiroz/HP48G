#variáveis
valores = []
vInt = False
quantDig = 0
operacoes = ["1 para Soma", "2 para Subtração", "3 para Multiplicação", "4 para Divisão"]
operacao = 0
valorFinal = 0
lV = 0
lO = 0
operadorVal = False

print("CÁLCULADORA HP48G")

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

#salva valores digitados pelo usuário no array
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

#mostra as operações disponíveis
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

#Não finalizado
def subtracao():
    while len(valores) > 1:
        calc = valores.pop() - valores.pop()
        valores.append(calc)

def multiplicacao():
    while len(valores) > 1:
        calc = valores.pop() * valores.pop()
        valores.append(calc)

#Não finalizado
def divisao():
    while len(valores) > 1:
        calc = valores.pop() / valores.pop()
        valores.append(calc)

if operacao == 1:
    soma()
    print("Resultado: " + str(valores[0]))

elif operacao == 2:
    #subtracao()
    print("Não definido")
    #print("Resultado: " + str(valores[0]))

elif operacao == 3:
    multiplicacao()
    print("Resultado: " + str(valores[0]))

elif operacao == 4:
    divisao()
    #print("Não definido")
    print("Resultado: " + str(valores[0]))