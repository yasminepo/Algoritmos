import random
num=random.randint(1, 10)
y=0
while y<3:
  x=int(input("Um número inteiro de 1 a 10: "))
  y+=1
  if x==num:
    print("Parabéns, você acertou!")
    break
  if y<3:
    if x<num:
        print('Você errou! Tente um número maior')
    else:
        print('Você errou! Tente um número menor')
  if y==3 and x!=num:
    print("Você perdeu! Fim de jogo.")
  
