print("       Calculadora de números reais       \n"
"1. Soma\n"
"2. Subtração\n"
"3. Multiplicação\n"
'4. Divisão')

print("")
x=input("Digite o número da operação desejada: ")  
if x == "1":
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))

    adição= num1+num2
    print("Resultado da soma: ", adição)
    
if x == "2":
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))

    subtração= num1-num2
    print("Resultado da subtração: ", subtração)

if x == "3":
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))

    multiplicação= num1*num2
    print("Resultado da multiplicação: ", multiplicação)

if x == "4":
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))

    divisão= num1/num2
    print("Resultado da divisão: ", divisão)