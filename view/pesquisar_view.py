
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
        st.rerun()v
from controller import usuario_controller


def tela_pesquisar():
    """
    Exibe a tela de pesquisa de usuário pelo login.
    """
    st.title("🔎 Pesquisar Usuário")

    login = st.text_input("Login a pesquisar")

    if st.button("Pesquisar"):
        encontrado, mensagem = usuario_controller.controlador_pesquisar_usuario(login)

        if encontrado:
            st.success(mensagem)
        else:
            st.warning(mensagem)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()
