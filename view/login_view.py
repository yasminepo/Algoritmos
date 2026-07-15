import streamlit as st
from controller import usuario_controller


def tela_remover():
    """
    Exibe a tela de remoção de usuário pelo login.
    """
    st.title("🗑️ Remover Usuário")

    login = st.text_input("Login a remover")

    if st.button("Remover"):
        sucesso, mensagem = usuario_controller.controlador_remover_usuario(login)

        if sucesso:
            st.success(mensagem)
        else:
            st.warning(mensagem)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()
from controller import usuario_controller


def tela_login():
    """
    Exibe a tela inicial de login do sistema.
    """
    st.title("🔐 Sistema de Cadastro de Usuários")
    st.header("Login")

    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        
        login_valido = usuario_controller.controlador_login(login, senha)

        if login_valido:
           
            st.session_state.autenticado = True
            st.session_state.usuario_logado = login
            st.session_state.tela = "menu"
            st.rerun()
        else:
            st.error("Login ou senha incorretos.")

    st.info("Dica: o usuário administrador padrão é login **admin** e senha **123**.")
