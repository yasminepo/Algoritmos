rom model.banco_dados import usuarios

def inserir_usuario(login, senha):
   
    usuarios[login] = senha


def remover_usuario(login):
   
    if login in usuarios:
        del usuarios[login]
        return True
    return False


def pesquisar_usuario(login):
  
    if login in usuarios:
        return True
    return False


def listar_usuarios():
   
    lista_de_logins = []

    for login in usuarios:
        lista_de_logins.append(login)

    return lista_de_logins


def validar_login(login, senha):
  
    if login in usuarios and usuarios[login] == senha:
        return True
    return False
