import streamlit as st


def tela_menu():
   
    st.title("📋 Menu Principal")
    st.write(f"Usuário logado: **{st.session_state.usuario_logado}**")

    st.header("Escolha uma opção")

    if st.button("1️⃣ Inserir usuário"):
        st.session_state.tela = "inserir"
        st.rerun()

    if st.button("2️⃣ Pesquisar usuário"):
        st.session_state.tela = "pesquisar"
        st.rerun()

    if st.button("3️⃣ Remover usuário"):
        st.session_state.tela = "remover"
        st.rerun()

    if st.button("4️⃣ Listar todos os usuários"):
        st.session_state.tela = "listar"
        st.rerun()

    if st.button("5️⃣ Logout"):
    
        st.session_state.autenticado = False
        st.session_state.usuario_logado = ""
        st.session_state.tela = "login"
        st.rerun()
