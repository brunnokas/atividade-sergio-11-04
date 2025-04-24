import streamlit as st
import csv
import os

# ===============================
# Funções Auxiliares
# ===============================
def caminho_transacoes(usuario):
    return f"transacoes_{usuario}.csv"

def carregar_transacoes(usuario):
    caminho = caminho_transacoes(usuario)
    transacoes = []
    if os.path.exists(caminho):
        with open(caminho, mode="r", encoding="utf-8") as arq:
            reader = csv.DictReader(arq)
            for row in reader:
                transacoes.append({
                    "tipo": row["tipo"],
                    "categoria": row["categoria"],
                    "valor": float(row["valor"])
                })
    return transacoes

def salvar_transacoes(usuario, transacoes):
    with open(caminho_transacoes(usuario), mode="w", newline="", encoding="utf-8") as arq:
        writer = csv.DictWriter(arq, fieldnames=["tipo", "categoria", "valor"])
        writer.writeheader()
        writer.writerows(transacoes)

def usuario_existe(nome):
    if not os.path.exists("usuarios.txt"):
        return False
    with open("usuarios.txt", "r") as f:
        for linha in f:
            u, _ = linha.strip().split(",")
            if u == nome:
                return True
    return False

def autenticar(usuario, senha):
    if not os.path.exists("usuarios.txt"):
        return False
    with open("usuarios.txt", "r") as f:
        for linha in f:
            u, s = linha.strip().split(",")
            if u == usuario and s == senha:
                return True
    return False

def registrar_usuario(usuario, senha):
    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario},{senha}\n")

# ===============================
# Interface Streamlit
# ===============================

st.set_page_config(page_title="Controle Financeiro", layout="centered")
st.title("💰 Controle Financeiro Pessoal")

# Estado de sessão
if "usuario" not in st.session_state:
    st.session_state.usuario = None

# Login ou Cadastro
if not st.session_state.usuario:
    aba = st.sidebar.radio("Acesso", ["Login", "Cadastro"])

    if aba == "Login":
        st.subheader("🔐 Login")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if autenticar(usuario, senha):
                st.session_state.usuario = usuario
                st.experimental_rerun()
            else:
                st.error("Usuário ou senha inválidos.")

    elif aba == "Cadastro":
        st.subheader("📝 Cadastro de Novo Usuário")
        novo_usuario = st.text_input("Novo usuário")
        nova_senha = st.text_input("Nova senha", type="password")
        if st.button("Cadastrar"):
            if usuario_existe(novo_usuario):
                st.warning("Nome de usuário já cadastrado.")
            else:
                registrar_usuario(novo_usuario, nova_senha)
                st.success("Usuário cadastrado com sucesso! Faça o login.")

# Página Principal
else:
    st.sidebar.success(f"Logado como: {st.session_state.usuario}")
    if st.sidebar.button("Sair"):
        st.session_state.usuario = None
        st.experimental_rerun()

    transacoes = carregar_transacoes(st.session_state.usuario)

    st.subheader("Adicionar Transação")
    tipo = st.selectbox("Tipo", ["receita", "despesa"])
    categoria = st.text_input("Categoria")
    valor = st.number_input("Valor (R$)", min_value=0.01, format="%.2f")

    if st.button("Adicionar"):
        transacoes.append({"tipo": tipo, "categoria": categoria, "valor": valor})
        salvar_transacoes(st.session_state.usuario, transacoes)
        st.success("Transação registrada com sucesso!")

    st.subheader("Transações Registradas")
    if transacoes:
        st.table(transacoes)
    else:
        st.info("Nenhuma transação registrada ainda.")

    st.subheader("Saldo Atual")
    saldo = sum(t["valor"] if t["tipo"] == "receita" else -t["valor"] for t in transacoes)
    st.metric(label="Saldo (R$)", value=f"R$ {saldo:.2f}")

    st.subheader("Exportar CSV")
    nome_arquivo = st.text_input("Nome do arquivo para exportação", value="relatorio.csv")
    if st.button("Exportar"):
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tipo", "categoria", "valor"])
            writer.writeheader()
            writer.writerows(transacoes)
        st.success(f"Arquivo '{nome_arquivo}' exportado com sucesso!")
