import streamlit as st
import csv
import os

st.set_page_config(page_title="Controle Financeiro", layout="centered")

# ==============================
# Funções auxiliares
# ==============================

def caminho_transacoes():
    return f"transacoes_{st.session_state.usuario}.csv"

def carregar_transacoes():
    transacoes = []
    try:
        with open(caminho_transacoes(), mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transacoes.append({
                    "tipo": row["tipo"],
                    "categoria": row["categoria"],
                    "valor": float(row["valor"])
                })
    except FileNotFoundError:
        pass
    return transacoes

def salvar_transacoes(transacoes):
    with open(caminho_transacoes(), mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tipo", "categoria", "valor"])
        writer.writeheader()
        writer.writerows(transacoes)

# ==============================
# Login e Cadastro
# ==============================

def cadastrar_usuario():
    st.subheader("Cadastrar novo usuário")
    novo_usuario = st.text_input("Nome de usuário")
    nova_senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        if not novo_usuario or not nova_senha:
            st.warning("Preencha todos os campos.")
            return
        try:
            with open("usuarios.txt", "r") as f:
                for linha in f:
                    u, _ = linha.strip().split(",")
                    if u == novo_usuario:
                        st.error("Nome de usuário já cadastrado.")
                        return
        except FileNotFoundError:
            pass

        with open("usuarios.txt", "a") as f:
            f.write(f"{novo_usuario},{nova_senha}\n")
        st.success("Usuário cadastrado com sucesso!")


def fazer_login():
    st.subheader("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        try:
            with open("usuarios.txt", "r") as f:
                for linha in f:
                    u, s = linha.strip().split(",")
                    if u == usuario and s == senha:
                        st.session_state.logado = True
                        st.session_state.usuario = usuario
                        return
        except FileNotFoundError:
            st.error("Arquivo de usuários não encontrado.")
        st.error("Usuário ou senha inválidos.")

# ==============================
# Funções de Transações
# ==============================

def adicionar_transacao():
    st.subheader("Adicionar Transação")
    tipo = st.selectbox("Tipo", ["receita", "despesa"])
    categoria = st.text_input("Categoria")
    valor = st.number_input("Valor", min_value=0.01, step=0.01)
    if st.button("Salvar Transação"):
        transacoes = carregar_transacoes()
        transacoes.append({"tipo": tipo, "categoria": categoria, "valor": valor})
        salvar_transacoes(transacoes)
        st.success("Transação salva com sucesso!")


def listar_transacoes():
    st.subheader("Minhas Transações")
    transacoes = carregar_transacoes()
    if transacoes:
        for i, t in enumerate(transacoes, start=1):
            st.write(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")
    else:
        st.info("Nenhuma transação registrada.")


def ver_saldo():
    transacoes = carregar_transacoes()
    saldo = sum(t["valor"] if t["tipo"] == "receita" else -t["valor"] for t in transacoes)
    st.subheader(f"Saldo Atual: R$ {saldo:.2f}")


def filtrar_transacoes():
    transacoes = carregar_transacoes()
    st.subheader("Filtrar Transações")
    filtro = st.selectbox("Filtrar por", ["tipo", "categoria"])
    valor = st.text_input("Valor do filtro")
    filtradas = [t for t in transacoes if t[filtro].lower() == valor.lower()]
    if filtradas:
        for i, t in enumerate(filtradas, start=1):
            st.write(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")
    else:
        st.warning("Nenhuma transação encontrada.")


def exportar_csv():
    transacoes = carregar_transacoes()
    if transacoes:
        with open("exportado.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tipo", "categoria", "valor"])
            writer.writeheader()
            writer.writerows(transacoes)
        st.success("Arquivo exportado como 'exportado.csv'")
    else:
        st.warning("Nenhuma transação para exportar.")

# ==============================
# Interface Principal
# ==============================

def menu_principal():
    st.title("💼 Controle Financeiro Pessoal")

    if "logado" not in st.session_state:
        st.session_state.logado = False
        st.session_state.usuario = ""

    if not st.session_state.logado:
        aba = st.radio("Selecione uma opção:", ["Login", "Cadastrar"])
        if aba == "Login":
            fazer_login()
        else:
            cadastrar_usuario()
    else:
        st.success(f"Logado como: {st.session_state.usuario}")
        opcao = st.selectbox("Menu", [
            "Adicionar Transação",
            "Listar Transações",
            "Ver Saldo",
            "Filtrar Transações",
            "Exportar CSV",
            "Sair"
        ])

        if opcao == "Adicionar Transação":
            adicionar_transacao()
        elif opcao == "Listar Transações":
            listar_transacoes()
        elif opcao == "Ver Saldo":
            ver_saldo()
        elif opcao == "Filtrar Transações":
            filtrar_transacoes()
        elif opcao == "Exportar CSV":
            exportar_csv()
        elif opcao == "Sair":
            st.session_state.logado = False
            st.session_state.usuario = ""
            st.experimental_rerun()

menu_principal()
