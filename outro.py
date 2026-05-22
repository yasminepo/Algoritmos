while True:
    print("Formas de pagamento")
    print("1. Á vista (em espécie): 15% de desconto")
    print("2. Cartão de débito: 10% de desconto")
    print("3. Cartão de crédito (vencimento): 5% de desconto")
    print("0. Sair")

    y=float(input("Preço total da venda: "))
    x=int(input("Forma de pagamento: "))

    if x>0:
        if x == 1:
            desconto1=y*0.15
            vf1=y-desconto1
            print("Valor final a ser pago: ", vf1)
        elif x == 2:
            desconto2=y*0.10
            vf2=y-desconto2
            print("Valor final a ser pago: ", vf2)
        elif x == 3:
            desconto3=y*0.05
            vf3=y-desconto3
            print("Valor final a ser pago: ", vf3)
        else:
            print("Forma de pagameto inválida!")
    else:
        break
        