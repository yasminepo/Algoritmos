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


def tela_inserir():
    
    st.title("➕ Inserir Usuário")

    login = st.text_input("Novo login")
    senha = st.text_input("Nova senha", type="password")

    if st.button("Cadastrar"):
        sucesso, mensagem = usuario_controller.controlador_inserir_usuario(login, senha)

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()
