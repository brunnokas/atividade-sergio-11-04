import csv
import os

# Variáveis globais
usuario_atual = None  # Variável para armazenar o usuário atualmente logado
transacoes = []  # Lista para armazenar as transações do usuário

# ==============================
# Cadastro e Login de Usuário
# ==============================

def cadastrar_usuario():
    print("============= Cadastro de Usuário =============")
    usuario = input("Digite o nome de usuário: ")  # Solicita o nome do usuário

    # Verifica se o nome de usuário já existe no arquivo
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                u, s = linha.strip().split(",")  # Divide a linha em nome de usuário e senha
                if u == usuario:  # Se o nome de usuário já estiver cadastrado
                    print("Nome de usuário já cadastrado.")  # Informa que o nome já existe
                    if input("Deseja tentar novamente? (s/n): ").lower() == 'n':  # Pergunta se quer tentar novamente
                        return
                    else:
                        return cadastrar_usuario()  # Chama a função novamente para tentar o cadastro
    except FileNotFoundError:
        pass  # Caso o arquivo de usuários não exista, continua para o cadastro

    senha = input("Digite a senha: ")  # Solicita a senha do novo usuário

    # Cadastra o novo usuário no arquivo
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{senha}\n")  # Escreve o nome de usuário e senha no arquivo
    print("Usuário cadastrado com sucesso!")

def login():
    global usuario_atual, transacoes  # Acessa as variáveis globais
    print("============= Login =============")
    while True:
        usuario = input("Digite o nome de usuário: ")  # Solicita o nome do usuário
        senha = input("Digite a senha: ")  # Solicita a senha

        try:
            with open("usuarios.txt", "r") as arquivo:  # Tenta abrir o arquivo de usuários
                for linha in arquivo:
                    u, s = linha.strip().split(",")  # Divide a linha em nome de usuário e senha
                    if u == usuario and s == senha:  # Verifica se as credenciais estão corretas
                        usuario_atual = usuario  # Define o usuário atual como o usuário logado
                        print(f"Login bem-sucedido! Bem-vindo, {usuario}!")  # Mensagem de sucesso
                        carregar_transacoes()  # Carrega as transações do usuário
                        menu_interno()  # Chama o menu interno de transações
                        return
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Cadastre um usuário primeiro.")  # Se o arquivo não existir
            return

        print("Usuário ou senha inválidos. Tente novamente.")  # Mensagem de erro
        if input("Deseja tentar novamente? (s/n): ").lower() == 'n':  # Pergunta se o usuário quer tentar novamente
            break

# ==============================
# Arquivo de Transações por Usuário
# ==============================

def caminho_arquivo_usuario():
    return f"transacoes_{usuario_atual}.csv"  # Gera o caminho do arquivo de transações com o nome do usuário

def carregar_transacoes():
    global transacoes  # Acessa a variável global
    transacoes = []  # Limpa a lista de transações

    try:
        with open(caminho_arquivo_usuario(), mode="r", encoding="utf-8") as arquivo:  # Tenta abrir o arquivo de transações
            reader = csv.DictReader(arquivo)  # Lê o arquivo CSV
            for row in reader:
                transacoes.append({
                    "tipo": row["tipo"],
                    "categoria": row["categoria"],
                    "valor": float(row["valor"])  # Converte o valor para float
                })
    except FileNotFoundError:
        pass  # Se o arquivo não existir, não faz nada (nenhuma transação foi registrada ainda)

def salvar_transacoes():
    with open(caminho_arquivo_usuario(), mode="w", newline="", encoding="utf-8") as arquivo:
        campos = ["tipo", "categoria", "valor"]  # Define os campos do CSV
        writer = csv.DictWriter(arquivo, fieldnames=campos)  # Cria o escritor do CSV
        writer.writeheader()  # Escreve o cabeçalho do CSV
        writer.writerows(transacoes)  # Escreve as transações no arquivo

# ==============================
# Transações
# ==============================

def adicionar_transacao():
    if not usuario_atual:  # Verifica se o usuário está logado
        print("Erro: Nenhum usuário logado.")
        return

    tipo = input("Digite o tipo (receita/despesa): ").strip().lower()  # Solicita o tipo da transação
    if tipo not in ['receita', 'despesa']:  # Verifica se o tipo é válido
        print("Tipo inválido. Use 'receita' ou 'despesa'.")
        return

    categoria = input("Digite a categoria (ex: alimentação, transporte): ").strip()  # Solicita a categoria
    try:
        valor = float(input("Digite o valor: "))  # Solicita o valor da transação
        if valor <= 0:  # Verifica se o valor é positivo
            print("O valor deve ser positivo.")
            return
    except ValueError:
        print("Valor inválido. Use apenas números.")  # Caso o valor não seja um número válido
        return

    transacoes.append({"tipo": tipo, "categoria": categoria, "valor": valor})  # Adiciona a transação à lista
    salvar_transacoes()  # Salva as transações no arquivo
    print("Transação registrada com sucesso!")

def listar_transacoes():
    if not usuario_atual:  # Verifica se o usuário está logado
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    print("\n=== Lista de Transações ===")
    for i, t in enumerate(transacoes, start=1):  # Lista as transações
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")

def ver_saldo():
    if not usuario_atual:  # Verifica se o usuário está logado
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    saldo = 0
    for t in transacoes:
        if t["tipo"] == "receita":  # Adiciona as receitas ao saldo
            saldo += t["valor"]
        elif t["tipo"] == "despesa":  # Subtrai as despesas do saldo
            saldo -= t["valor"]

    print(f"\nSaldo atual: R$ {saldo:.2f}")  # Exibe o saldo final

def filtrar_transacoes():
    if not usuario_atual:  # Verifica se o usuário está logado
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    filtro = input("Filtrar por (tipo/categoria): ").strip().lower()  # Solicita o filtro
    if filtro not in ['tipo', 'categoria']:  # Verifica se o filtro é válido
        print("Filtro inválido.")
        return

    valor_filtro = input("Digite o valor do filtro: ").strip().lower()  # Solicita o valor do filtro
    filtradas = [t for t in transacoes if t[filtro].lower() == valor_filtro]  # Filtra as transações

    if not filtradas:  # Se não encontrar transações que atendem ao filtro
        print("Nenhuma transação encontrada.")
        return

    print("\n=== Transações Filtradas ===")
    for i, t in enumerate(filtradas, start=1):  # Exibe as transações filtradas
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")

def exportar_csv():
    if not usuario_atual:  # Verifica se o usuário está logado
        print("Erro: Nenhum usuário logado.")
        return

    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação para exportar.")
        return

    nome_arquivo = input("Digite o nome do arquivo (ex: relatorio.csv): ")  # Solicita o nome do arquivo para exportação
    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            campos = ["tipo", "categoria", "valor"]  # Define os campos do CSV
            writer = csv.DictWriter(arquivo, fieldnames=campos)  # Cria o escritor do CSV
            writer.writeheader()  # Escreve o cabeçalho
            writer.writerows(transacoes)  # Escreve as transações
        print(f"Transações exportadas com sucesso para '{nome_arquivo}'!")
    except Exception as e:
        print(f"Erro ao exportar: {e}")  # Exibe erro se ocorrer ao tentar exportar

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
            adicionar_transacao()  # Chama a função para adicionar transação
        elif opcao == "2":
            listar_transacoes()  # Chama a função para listar transações
        elif opcao == "3":
            ver_saldo()  # Chama a função para ver o saldo
        elif opcao == "4":
            filtrar_transacoes()  # Chama a função para filtrar transações
        elif opcao == "5":
            exportar_csv()  # Chama a função para exportar transações
        elif opcao == "6":
            print(f"Saindo da conta de {usuario_atual}...\n")  # Exibe mensagem de saída
            break
        else:
            print("Opção inválida. Tente novamente.")  # Exibe mensagem de erro

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
            cadastrar_usuario()  # Chama a função para cadastrar um novo usuário
        elif opcao == "2":
            login()  # Chama a função para fazer login
        elif opcao == "3":
            print("Saindo do programa...")  # Exibe mensagem de saída
            break
        else:
            print("Opção inválida. Tente novamente.")  # Exibe mensagem de erro

# Iniciar o programa
menu_principal()
