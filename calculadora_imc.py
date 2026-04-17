num1= float(input('Seu peso (em kg): '))
num2= float(input("Sua altura (em m): "))

imc= num1/num2**2

print(f'Resultado do IMC: {imc}kg/m²')

if imc > 40:
    print("Obesidade grave")
elif imc > 29.9:
    print("Obesidade")
elif imc > 24.9:
    print("Sobrepeso")    
elif imc > 18.4:
    print("Peso normal")    
else:
    print("Magreza")
