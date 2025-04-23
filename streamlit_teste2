import streamlit as st
import pandas as pd
import os

# Carregar usuários
def carregar_usuarios():
    if not os.path.exists("usuarios.txt"):
        return {}
    with open("usuarios.txt", "r") as arquivo:
        return dict(linha.strip().split(",") for linha in arquivo.readlines())

# Salvar usuário
def salvar_usuario(usuario, senha):
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{senha}\n")

# Autenticação
def autenticar(usuario, senha):
    usuarios = carregar_usuarios()
    return usuarios.get(usuario) == senha

# Inicializar lista de transações
if 'transacoes' not in st.session_state:
    st.session_state.transacoes = []

# Inicializar status de login
if 'logado' not in st.session_state:
    st.session_state.logado = False

# Página de login/cadastro
st.title("💰 Controle de Finanças Pessoais")

menu = ["Login", "Cadastro"]
escolha = st.sidebar.selectbox("Menu", menu)

# Tela de Cadastro
if escolha == "Cadastro":
    st.subheader("📋 Cadastro de Usuário")
    novo_usuario = st.text_input("Usuário")
    nova_senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        usuarios = carregar_usuarios()
        if novo_usuario in usuarios:
            st.error("Usuário já existe!")
        else:
            salvar_usuario(novo_usuario, nova_senha)
            st.success("Usuário cadastrado com sucesso!")

# Tela de Login
elif escolha == "Login":
    st.subheader("🔐 Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state.logado = True
            st.success("Login bem-sucedido!")

# Após login bem-sucedido
if st.session_state.logado:
    st.subheader("📌 Menu de Funcionalidades")

    # Adicionar transação
    st.markdown("### ➕ Adicionar Transação")
    tipo = st.selectbox("Tipo", ["receita", "despesa"])
    categoria = st.text_input("Categoria")
    valor = st.number_input("Valor", min_value=0.01)
    if st.button("Adicionar"):
        st.session_state.transacoes.append({
            "tipo": tipo,
            "categoria": categoria,
            "valor": valor
        })
        st.success("Transação adicionada com sucesso!")

    # Listar transações
    if st.session_state.transacoes:
        st.markdown("### 📜 Transações Registradas")
        df = pd.DataFrame(st.session_state.transacoes)

        # Exibição formatada
        df_visual = df.sort_values(by="valor", ascending=False).reset_index(drop=True)
        df_visual.index = df_visual.index + 1  # Index começa do 1
        df_visual["valor"] = df_visual["valor"].apply(lambda x: f"{x:,.0f}".replace(",", "."))

        st.dataframe(df_visual)

        # Saldo
        receitas = sum(t['valor'] for t in st.session_state.transacoes if t['tipo'] == 'receita')
        despesas = sum(t['valor'] for t in st.session_state.transacoes if t['tipo'] == 'despesa')
        saldo = receitas - despesas
        st.info(f"💼 Saldo Atual: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

        # Filtro
        st.markdown("### 🔎 Filtrar Transações")
        filtro_tipo = st.selectbox("Filtrar por tipo", ["", "receita", "despesa"])
        filtro_cat = st.text_input("Filtrar por categoria")
        filtradas = df
        if filtro_tipo:
            filtradas = filtradas[filtradas["tipo"] == filtro_tipo]
        if filtro_cat:
            filtradas = filtradas[filtradas["categoria"].str.lower() == filtro_cat.lower()]
        if not filtradas.empty:
            st.dataframe(filtradas)
        else:
            st.warning("Nenhuma transação encontrada com os filtros.")

        # Exportar CSV formatado
        st.markdown("### 📤 Exportar Dados")
        df_export = df.sort_values(by="valor", ascending=False).reset_index(drop=True)
        df_export.index = df_export.index + 1
        csv = df_export.to_csv(index_label="", encoding="utf-8-sig")
        st.download_button("Baixar CSV", data=csv, file_name="transacoes.csv", mime="text/csv")
