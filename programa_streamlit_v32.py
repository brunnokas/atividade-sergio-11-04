import streamlit as st
import csv
import os

# Função de cadastro de usuário
def cadastrar_usuario():
    nome_usuario = st.text_input("Digite o nome de usuário:")
    senha = st.text_input("Digite a senha:", type="password")
    
    if st.button("Cadastrar"):
        if nome_usuario and senha:
            # Verifica se o arquivo de usuários existe
            if os.path.exists("usuarios.txt"):
                with open("usuarios.txt", "r") as f:
                    usuarios = f.readlines()
                    for usuario in usuarios:
                        if nome_usuario in usuario:
                            st.error("Nome de usuário já cadastrado.")
                            return
            
            with open("usuarios.txt", "a") as f:
                f.write(f"{nome_usuario},{senha}\n")
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

# Função de login de usuário
def login_usuario():
    nome_usuario = st.text_input("Digite o nome de usuário:")
    senha = st.text_input("Digite a senha:", type="password")
    
    if st.button("Login"):
        if nome_usuario and senha:
            # Verifica se o arquivo de usuários existe
            if os.path.exists("usuarios.txt"):
                with open("usuarios.txt", "r") as f:
                    usuarios = f.readlines()
                    for usuario in usuarios:
                        u_nome, u_senha = usuario.strip().split(",")
                        if u_nome == nome_usuario and u_senha == senha:
                            st.success(f"Login bem-sucedido! Bem-vindo, {nome_usuario}!")
                            return nome_usuario
                st.error("Credenciais inválidas.")
            else:
                st.error("Nenhum usuário cadastrado.")
        else:
            st.error("Por favor, preencha todos os campos.")
    return None

# Funções de transações
def adicionar_transacao(usuario):
    tipo = st.selectbox("Selecione o tipo de transação:", ["receita", "despesa"])
    categoria = st.text_input("Categoria (ex: alimentação, transporte):")
    valor = st.number_input("Valor:", min_value=0.01, step=0.01)

    if st.button("Adicionar Transação"):
        if tipo and categoria and valor:
            with open(f"transacoes_{usuario}.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([tipo, categoria, valor])
            st.success("Transação registrada com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

def listar_transacoes(usuario):
    if os.path.exists(f"transacoes_{usuario}.csv"):
        with open(f"transacoes_{usuario}.csv", "r") as f:
            transacoes = f.readlines()
            if transacoes:
                st.write("### Lista de Transações:")
                for i, transacao in enumerate(transacoes, 1):
                    tipo, categoria, valor = transacao.strip().split(",")
                    st.write(f"{i}. Tipo: {tipo}, Categoria: {categoria}, Valor: R$ {valor}")
            else:
                st.write("Nenhuma transação registrada.")
    else:
        st.write("Nenhuma transação registrada.")

def ver_saldo(usuario):
    saldo = 0
    if os.path.exists(f"transacoes_{usuario}.csv"):
        with open(f"transacoes_{usuario}.csv", "r") as f:
            transacoes = f.readlines()
            for transacao in transacoes:
                tipo, _, valor = transacao.strip().split(",")
                valor = float(valor)
                if tipo == "receita":
                    saldo += valor
                elif tipo == "despesa":
                    saldo -= valor
    st.write(f"### Saldo Atual: R$ {saldo:.2f}")

def exportar_csv(usuario):
    if os.path.exists(f"transacoes_{usuario}.csv"):
        with open(f"transacoes_{usuario}.csv", "r") as f:
            transacoes = f.readlines()
            if transacoes:
                st.download_button(
                    label="Baixar Transações",
                    data="".join(transacoes),
                    file_name=f"transacoes_{usuario}.csv",
                    mime="text/csv"
                )
            else:
                st.write("Nenhuma transação registrada.")
    else:
        st.write("Nenhuma transação registrada.")

# Função principal para navegação
def app():
    st.title("Sistema de Controle Financeiro Pessoal")

    menu = ["Cadastro", "Login"]
    escolha = st.sidebar.selectbox("Escolha uma opção", menu)

    if escolha == "Cadastro":
        st.subheader("Cadastrar Novo Usuário")
        cadastrar_usuario()

    elif escolha == "Login":
        st.subheader("Login de Usuário")
        usuario_logado = login_usuario()

        if usuario_logado:
            st.sidebar.write(f"Bem-vindo, {usuario_logado}!")
            menu_interno(usuario_logado)

def menu_interno(usuario):
    st.subheader("Menu de Transações")
    menu_transacao = ["Adicionar Transação", "Listar Transações", "Ver Saldo", "Exportar CSV", "Sair"]
    escolha_transacao = st.sidebar.selectbox("Escolha uma opção", menu_transacao)

    if escolha_transacao == "Adicionar Transação":
        adicionar_transacao(usuario)
    elif escolha_transacao == "Listar Transações":
        listar_transacoes(usuario)
    elif escolha_transacao == "Ver Saldo":
        ver_saldo(usuario)
    elif escolha_transacao == "Exportar CSV":
        exportar_csv(usuario)
    elif escolha_transacao == "Sair":
        st.sidebar.write("Você saiu.")
        app()

if __name__ == "__main__":
    app()
