💼 Sistema de Controle Financeiro Pessoal
📅 Atividade Individual – 11/04
Trabalho em grupo do Sérgio — Para 25/04

🧠 Explicações das Funcionalidades do Código

🔐 Cadastro e Login de Usuário

cadastrar_usuario()
Solicita um nome de usuário e uma senha ao usuário. Esses dados são armazenados no arquivo usuarios.txt para uso posterior.

login()
Verifica se as credenciais inseridas coincidem com as registradas no arquivo usuarios.txt. Se o login for bem-sucedido, o sistema direciona o usuário ao menu interno.

💰 Funções de Transações

adicionar_transacao()
Permite ao usuário registrar uma nova transação do tipo "receita" ou "despesa", informando também a categoria e o valor.

listar_transacoes()
Exibe todas as transações registradas até o momento, organizadas em uma lista numerada.

ver_saldo()
Calcula o saldo atual com base nas transações realizadas, somando as receitas e subtraindo as despesas.

filtrar_transacoes()
Possibilita filtrar as transações de acordo com o tipo (receita/despesa) ou a categoria definida pelo usuário.

exportar_csv()
Gera um arquivo CSV com todas as transações registradas, utilizando o nome de arquivo fornecido pelo usuário.

🧭 Menu Interno

menu_interno()
Apresenta as opções disponíveis após o login: adicionar transações, listar transações, consultar o saldo, aplicar filtros ou exportar os dados para CSV. O menu permanece em execução até que o usuário opte por sair.

🏠 Menu Principal

O menu principal oferece as opções de cadastro, login ou sair do sistema. Ele funciona em loop, permitindo múltiplas interações com o usuário.


✅ Resumo Geral das Funcionalidades

✅ Cadastro e autenticação de usuários

✅ Registro de transações financeiras (receitas e despesas)

✅ Visualização de todas as transações realizadas

✅ Cálculo do saldo atual com base nas movimentações

✅ Filtro de transações por tipo ou categoria

✅ Exportação dos dados financeiros para um arquivo CSV

✅ Navegação simples e interativa através de menus
