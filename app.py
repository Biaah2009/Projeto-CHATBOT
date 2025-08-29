import streamlit as st
import pandas as pd
from database import criar_tabela, inserir_funcionarios,listar_funcionarios

criar_tabela()
st.set_page_config(page_title="Cadastro funcionario", page_icon="👾")
st.title("cadastro de funcionarios" )

with st.form("form_funcionarios", clear_on_submit=True):
    nome = st.text_input("nome")
    cargo = st.text_input("cargo")
    email = st.text_input("email")

    submit = st.form_submit_button("adicionar")

    if submit:
        if nome and cargo and email:
            try:
                inserir_funcionarios(nome,cargo,email)
                st.success(f"funcionario {nome} adicionado!")
            except Exception as e:
                st.error(f"erro: {e}")
        else:
            st.warning("preencha todos os campos")

st.subheader("listar_funcionarios")

dados = listar_funcionarios()
if dados:
    df = pd.DataFrame(dados, columns=["ID","nome","cargo","email"])
    st.dataframe(df,use_container_width=True)
else:
    st.info("nenhum funcionario cadastrado")