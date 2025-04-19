import csv  # Importa a biblioteca csv para manipular arquivos CSV

# Lista global de transações
transacoes = []  # Lista que armazenará todas as transações realizadas

# ==============================
# Cadastro e Login de Usuário
# ==============================

def cadastrar_usuario():
    print("============= Cadastro de Usuário =============")
    usuario = input("Digite o nome de usuário: ")  # Solicita o nome de usuário
    senha = input("Digite a senha: ")  # Solicita a senha

    # Abre o arquivo "usuarios.txt" em modo de append ('a') para adicionar novos usuários
    with open("usuarios.txt", "a") as arquivo:
        # Escreve o nome de usuário e a senha no arquivo separados por vírgula
        arquivo.write(f"{usuario},{senha}\n")
        print("Usuário cadastrado com sucesso!")  # Confirma que o usuário foi cadastrado

def login():
    print("============= Login =============")
    while True:
        usuario = input("Digite o nome de usuário: ")  # Solicita o nome de usuário
        senha = input("Digite a senha: ")  # Solicita a senha

        try:
            # Abre o arquivo "usuarios.txt" em modo de leitura ('r') para verificar as credenciais
            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:  # Para cada linha do arquivo
                    u, s = linha.strip().split(",")  # Divide a linha em nome de usuário e senha
                    if u == usuario and s == senha:  # Verifica se os dados coincidem
                        print("Login bem-sucedido!")  # Login bem-sucedido
                        menu_interno()  # Chama o menu de opções após o login
                        return
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Cadastre um usuário primeiro.")
            return

        print("Usuário ou senha inválidos. Tente novamente.\n")  # Mensagem de erro se o login falhar
        if input("Deseja tentar novamente? (s/n): ").lower() == 'n':  # Permite que o usuário tente novamente ou saia
            break

# ==============================
# Transações
# ==============================

def adicionar_transacao():
    tipo = input("Digite o tipo (receita/despesa): ").strip().lower()  # Solicita o tipo da transação (receita ou despesa)
    if tipo not in ['receita', 'despesa']:  # Verifica se o tipo é válido
        print("Tipo inválido. Use 'receita' ou 'despesa'.")
        return

    categoria = input("Digite a categoria (ex: alimentação, transporte): ").strip()  # Solicita a categoria da transação
    try:
        valor = float(input("Digite o valor: "))  # Solicita o valor e tenta convertê-lo para float
        if valor <= 0:  # Verifica se o valor é maior que 0
            print("O valor deve ser positivo.")
            return
    except ValueError:  # Caso o valor não seja numérico, exibe uma mensagem de erro
        print("Valor inválido. Use apenas números.")
        return

    # Adiciona a transação na lista global de transações
    transacoes.append({"tipo": tipo, "categoria": categoria, "valor": valor})
    print("Transação registrada com sucesso!")  # Confirma a adição da transação

def listar_transacoes():
    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    print("\n=== Lista de Transações ===")
    for i, t in enumerate(transacoes, start=1):  # Enumera as transações começando do 1
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")  # Exibe cada transação

def ver_saldo():
    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    saldo = 0  # Inicializa a variável saldo
    for t in transacoes:  # Itera por todas as transações
        if t["tipo"] == "receita":  # Se a transação for uma receita, soma o valor
            saldo += t["valor"]
        elif t["tipo"] == "despesa":  # Se a transação for uma despesa, subtrai o valor
            saldo -= t["valor"]

    print(f"\nSaldo atual: R$ {saldo:.2f}")  # Exibe o saldo atual com duas casas decimais

def filtrar_transacoes():
    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação registrada.")
        return

    filtro = input("Filtrar por (tipo/categoria): ").strip().lower()  # Solicita o tipo de filtro (tipo ou categoria)
    if filtro not in ['tipo', 'categoria']:  # Verifica se o filtro é válido
        print("Filtro inválido.")
        return

    valor_filtro = input("Digite o valor do filtro: ").strip().lower()  # Solicita o valor do filtro
    # Filtra as transações de acordo com o filtro e valor fornecidos
    filtradas = [t for t in transacoes if t[filtro].lower() == valor_filtro]

    if not filtradas:  # Se não houver transações que atendem ao filtro
        print("Nenhuma transação encontrada.")
        return

    print("\n=== Transações Filtradas ===")
    for i, t in enumerate(filtradas, start=1):  # Exibe as transações filtradas
        print(f"{i}. Tipo: {t['tipo'].capitalize()}, Categoria: {t['categoria']}, Valor: R$ {t['valor']:.2f}")

def exportar_csv():
    if not transacoes:  # Verifica se não há transações
        print("Nenhuma transação para exportar.")
        return

    nome_arquivo = input("Digite o nome do arquivo (ex: relatorio.csv): ")  # Solicita o nome do arquivo CSV
    try:
        # Abre o arquivo em modo de escrita ('w') e configura o writer para escrever no formato CSV
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            campos = ["tipo", "categoria", "valor"]  # Define os campos que serão exportados
            writer = csv.DictWriter(arquivo, fieldnames=campos)  # Cria o objeto writer
            writer.writeheader()  # Escreve o cabeçalho no arquivo CSV
            writer.writerows(transacoes)  # Escreve as transações no arquivo CSV
        print(f"Transações exportadas com sucesso para '{nome_arquivo}'!")  # Confirma que as transações foram exportadas
    except Exception as e:  # Captura qualquer erro durante o processo de exportação
        print(f"Erro ao exportar: {e}")  # Exibe o erro ocorrido

# ==============================
# Menu Interno
# ==============================

def menu_interno():
    while True:
        # Exibe o menu de opções para o usuário
        print("\n========= MENU DE TRANSAÇÕES =========")
        print("1. Adicionar transação")
        print("2. Listar transações")
        print("3. Ver saldo atual")
        print("4. Filtrar transações")
        print("5. Exportar para CSV")
        print("6. Sair do sistema")

        opcao = input("Escolha uma opção: ")  # Solicita ao usuário uma opção do menu

        if opcao == "1":
            adicionar_transacao()  # Chama a função para adicionar uma transação
        elif opcao == "2":
            listar_transacoes()  # Chama a função para listar transações
        elif opcao == "3":
            ver_saldo()  # Chama a função para ver o saldo
        elif opcao == "4":
            filtrar_transacoes()  # Chama a função para filtrar transações
        elif opcao == "5":
            exportar_csv()  # Chama a função para exportar transações para CSV
        elif opcao == "6":
            print("Saindo do sistema...")  # Sai do sistema
            break
        else:
            print("Opção inválida. Tente novamente.")  # Exibe mensagem caso a opção seja inválida

# ==============================
# Menu Principal
# ==============================

while True:
    # Exibe o menu principal
    print("\n============= MENU PRINCIPAL =============")
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")  # Solicita ao usuário uma opção do menu principal

    if opcao == "1":
        cadastrar_usuario()  # Chama a função para cadastrar um usuário
    elif opcao == "2":
        login()  # Chama a função para realizar o login
    elif opcao == "3":
        print("Saindo do programa...")  # Sai do programa
        break
    else:
        print("Opção inválida. Tente novamente.")  # Exibe mensagem caso a opção seja inválida
