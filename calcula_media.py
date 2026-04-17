num1= float(input("Digite a primeira nota: "))
num2= float(input("Digite a segunda nota: "))
num3= float(input("Digite a terceira nota: "))


média= (num1+num2+num3)/3

print("Resultado da média: ", média)

if média >= 7:
    print("Aprovado")
else:
    print("Reprovado")