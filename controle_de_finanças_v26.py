import csv
import os

# Variáveis globais
usuario_atual = None
transacoes = []

# ==============================
# Cadastro e Login de Usuário
# ==============================

def cadastrar_usuario():
    print("============= Cadastro de Usuário =============")
    usuario = input("Digite o nome de usuário: ")

    # Verifica se o nome de usuário já existe no arquivo
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                u, s = linha.strip().split(",")
                if u == usuario:
                    print("Nome de usuário já cadastrado.")
                    if input("Deseja tentar novamente? (s/n): ").lower() == 'n':
                        return
                    else:
                        return cadastrar_usuario()  # Chama a função novamente
    except FileNotFoundError:
        pass  # Arquivo de usuários não encontrado, vamos criar um novo

    senha = input("Digite a senha: ")

    # Cadastra o novo usuário
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{senha}\n")
    print("Usuário cadastrado com sucesso!")

def login():
    global usuario_atual, transacoes
    print("============= Login =============")
    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        try:
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    u, s = linha.strip().split(",")
                    if u == usuario and s == senha:
                        usuario_atual = usuario
                        print(f"Login bem-sucedido! Bem-vindo, {usuario}!")
                        carregar_transacoes()
                        menu_interno()
                        return
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Cadastre um usuário primeiro.")
            return

        print("Usuário ou senha inválidos. Tente novamente.")
        if input("Deseja tentar novamente? (s/n): ").lower() == 'n':
            break

# ==============================
# Arquivo de Transações por Usuário
# ==============================

def caminho_arquivo_usuario():
    return f"transacoes_{usuario_atual}.csv"

def carregar_transacoes():
    global transacoes
    transacoes = []

    try:
        with open(caminho_arquivo_usuario(), mode="r", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            for row in reader:
                transacoes.append({
                    "tipo": row["tipo"],
                    "categoria": row["categoria"],
                    "valor": float(row["valor"])
                })
    except FileNotFoundError:
        pass  # Nenhum dado ainda

def salvar_transacoes():
    with open(caminho_arquivo_usuario(), mode="w", newline="", encoding="utf-8") as arquivo:
        campos = ["tipo", "categoria", "valor"]
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(transacoes)

# ==============================
# Transações
# ==============================

def adicionar_transacao():
    if not usuario_atual:
        print("Erro: Nenhum usuário logado.")
        return

    tipo = input("Digite o tipo (receita/despesa): ").strip().lower()
    if tipo not in ['receita', 'despesa']:
        print("Tipo inválido. Use 'receita' ou 'despesa'.")
        return

    categoria = input("Digite a categoria (ex: alimentação, transporte): ").strip()
    try:
        valor = float(input("Digite o valor: "))
        if valor <= 0:
            print("O valor deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido. Use apenas números.")
        return

    transacoes.append({"tipo": tipo, "categoria": categoria, "valor": valor})
    salvar_transacoes()
    print("Transação registrada com sucesso!")

def listar_transacoes():
    if not usuario_atual:
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    print("\n=== Lista de Transações ===")
    for i, t in enumerate(transacoes, start=1):
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")

def ver_saldo():
    if not usuario_atual:
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    saldo = 0
    for t in transacoes:
        if t["tipo"] == "receita":
            saldo += t["valor"]
        elif t["tipo"] == "despesa":
            saldo -= t["valor"]

    print(f"\nSaldo atual: R$ {saldo:.2f}")

def filtrar_transacoes():
    if not usuario_atual:
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:
        print("Nenhuma transação registrada.")
        return

    filtro = input("Filtrar por (tipo/categoria): ").strip().lower()
    if filtro not in ['tipo', 'categoria']:
        print("Filtro inválido.")
        return

    valor_filtro = input("Digite o valor do filtro: ").strip().lower()
    filtradas = [t for t in transacoes if t[filtro].lower() == valor_filtro]

    if not filtradas:
        print("Nenhuma transação encontrada.")
        return

    print("\n=== Transações Filtradas ===")
    for i, t in enumerate(filtradas, start=1):
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")

def exportar_csv():
    if not usuario_atual:
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:
        print("Nenhuma transação para exportar.")
        return

    nome_arquivo = input("Digite o nome do arquivo (ex: relatorio.csv): ")
    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            campos = ["tipo", "categoria", "valor"]
            writer = csv.DictWriter(arquivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(transacoes)
        print(f"Transações exportadas com sucesso para '{nome_arquivo}'!")
    except Exception as e:
        print(f"Erro ao exportar: {e}")

# ==============================
# Menu Interno
# ==============================

def menu_interno():
    while True:
        print(f"\n========= MENU DE TRANSAÇÕES ({usuario_atual}) =========")
        print("1. Adicionar transação")
        print("2. Listar transações")
        print("3. Ver saldo atual")
        print("4. Filtrar transações")
        print("5. Exportar para CSV")
        print("6. Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_transacao()
        elif opcao == "2":
            listar_transacoes()
        elif opcao == "3":
            ver_saldo()
        elif opcao == "4":
            filtrar_transacoes()
        elif opcao == "5":
            exportar_csv()
        elif opcao == "6":
            print(f"Saindo da conta de {usuario_atual}...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ==============================
# Menu Principal
# ==============================

def menu_principal():
    while True:
        print("\n============= MENU PRINCIPAL =============")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu_principal()
