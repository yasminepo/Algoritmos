num1=int(input('Digite um número inteiro(a): '))
num2=int(input('Digite um número inteiro(b): '))
soma=0
if num1<num2:
    while num1<=num2:
        soma+=num1
        num1+=1  
    print('Soma dos números inteiros no intervalo [a,b]: ', soma)
else: 
    print("Erro! O primeiro número deve ser menor que o segundo.")