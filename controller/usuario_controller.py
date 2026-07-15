rom model import banco_dados


def controlador_login(login, senha):
   
    return banco_dados.validar_login(login, senha)


def controlador_inserir_usuario(login, senha):
  
    login = login.strip()
    senha = senha.strip()

    if login == "" or senha == "":
        return False, "Login e senha não podem ficar em branco."

    if banco_dados.pesquisar_usuario(login):
        return False, f"O login '{login}' já está cadastrado."

    banco_dados.inserir_usuario(login, senha)
    return True, f"Usuário '{login}' cadastrado com sucesso!"


def controlador_pesquisar_usuario(login):

    login = login.strip()

    if banco_dados.pesquisar_usuario(login):
        return True, f"Usuário encontrado: {login}"
    return False, f"Usuário '{login}' não foi encontrado."


def controlador_remover_usuario(login):
  
    login = login.strip()

    if login == "admin":
        return False, "Não é permitido remover o usuário administrador."

    if banco_dados.remover_usuario(login):
        return True, f"Usuário '{login}' removido com sucesso!"
    return False, f"Usuário '{login}' não foi encontrado."


def controlador_listar_usuarios():
   
    return banco_dados.listar_usuarios()
