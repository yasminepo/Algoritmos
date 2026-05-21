soma=0 
quantidade=0 
maior=0 
while True: 
    num=int(input("Digite um número inteiro positivo: ")) 
    if num<0: 
        break 
    quantidade+=1 
    soma+=num
    if num>maior: 
        maior=num 
print(soma) 
print(soma/quantidade)
print(maior)