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

#mostra as operações
while lO < 4:
    print(operacoes.pop(0))
    lO+=1
    
#filtro de entrada (operador) - não finalizado
while operadorVal == False:
    operacao = input("Insira o valor da operação que deseja realizar: ")

    if operacao != "1" or operacao != "2" or operacao != "3" or operacao != "4":
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

#salva valores digitados no array
while lV < quantDig:
    valorN = input("Insira o " + str(lV + 1) + "° valor: ")

    try: 
        int(valorN)
        valorN = int(valorN)
        valores.append(valorN)
        lV+=1

    except ValueError:
        try:
            float(valorN)
            valorN = float(valorN)
            valores.append(valorN)
            lV+=1

        except ValueError:
            print("Valor inválido. Insira um novo valor.")

#printa valores em tela
print("O comprimento do array é " + str(len(valores)))
print("Valores: " + str(valores))