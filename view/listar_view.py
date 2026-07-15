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


def tela_listar():
    """
    Exibe a tela com a lista de todos os logins cadastrados.
    """
    st.title("📄 Lista de Usuários")

    logins = usuario_controller.controlador_listar_usuarios()

    if len(logins) == 0:
        st.warning("Nenhum usuário cadastrado.")
    else:
        
        dados_para_tabela = []
        for login in logins:
            dados_para_tabela.append({"Login": login})

        st.table(dados_para_tabela)

    st.write("---")

    if st.button("⬅ Voltar ao menu"):
        st.session_state.tela = "menu"
        st.rerun()
