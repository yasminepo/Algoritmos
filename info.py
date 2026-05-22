salario=float(input("Salário do funcionário: ")) 
cargo=input("Cargo do funcionário: ") 
if cargo == "Programador de sistemas": 
    v1=(salario*0.3)+salario
    print("Novo salário: ", v1) 
elif cargo == "Analista de sistemas": 
    v2=(salario*0.2)+salario 
    print("Novo salário: ", v2) 
elif cargo == "Analista de banco de dados":
    v3=(salario*0.15)+salario 
    print("Novo salário: ", v3) 
else: print("Cargo inválido")