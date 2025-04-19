# atividade-individual-11-04
Trabalho do Sérgio em grupo, dia 11/04 para 25/04

Explicações de cada parte do código:
1. Cadastro e Login de Usuário:
cadastrar_usuario(): Pergunta ao usuário um nome de usuário e senha. O novo usuário é salvo no arquivo usuarios.txt.

login(): Verifica se o nome de usuário e senha fornecidos correspondem aos dados registrados no arquivo usuarios.txt. Se o login for bem-sucedido, o menu interno é acessado.

2. Funções de Transações:
adicionar_transacao(): Permite ao usuário adicionar uma transação do tipo receita ou despesa, com a categoria e o valor informados.

listar_transacoes(): Lista todas as transações registradas até o momento.

ver_saldo(): Calcula o saldo atual do usuário, considerando as receitas e despesas registradas.

filtrar_transacoes(): Permite ao usuário filtrar as transações com base no tipo (receita ou despesa) ou categoria.

exportar_csv(): Exporte as transações registradas para um arquivo CSV com o nome escolhido pelo usuário.

3. Menu Interno:
menu_interno(): Exibe o menu de operações após o login. O usuário pode escolher adicionar transações, listar transações, ver saldo, filtrar transações ou exportar para CSV.

4. Menu Principal:
O menu principal permite que o usuário se cadastre ou faça login. O sistema vai continuar executando até que o usuário escolha a opção de sair.

Resumo das Funcionalidades:
Cadastro e login de usuários.

Adição de transações (receitas ou despesas).

Exibição de todas as transações.

Cálculo do saldo com base nas receitas e despesas.

Filtragem de transações por tipo ou categoria.

Exportação das transações para um arquivo CSV.

Menu interativo para o usuário navegar pelas opções.
