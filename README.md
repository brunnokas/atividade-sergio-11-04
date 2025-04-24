# 💼 Sistema de Controle Financeiro Pessoal 📅

**Atividade Python – 11/04**  
**Trabalho em grupo do Sérgio — Para 25/04**
**Faculdade UNA DIVINÓPOLIS ; CURSO CIÊNCIAS DA COMPUTAÇÃO 1° Período**

## 🧠 Explicações das Funcionalidades do Código

### 🔐 **Cadastro e Login de Usuário**

- **`cadastrar_usuario()`**  
  Solicita um nome de usuário e uma senha ao usuário. Esses dados são armazenados no arquivo `usuarios.txt` para uso posterior.

- **`login()`**  
  Verifica se as credenciais inseridas coincidem com as registradas no arquivo `usuarios.txt`. Se o login for bem-sucedido, o sistema direciona o usuário ao menu interno. O sistema também verifica se o nome de usuário já está registrado, impedindo duplicidade.

### 💰 **Funções de Transações**

- **`adicionar_transacao()`**  
  Permite ao usuário registrar uma nova transação do tipo "receita" ou "despesa", informando também a categoria e o valor. A transação é registrada no arquivo CSV associado ao usuário.

- **`listar_transacoes()`**  
  Exibe todas as transações registradas até o momento, organizadas em uma lista numerada. Cada transação é detalhada com tipo, categoria e valor.

- **`ver_saldo()`**  
  Calcula o saldo atual com base nas transações realizadas, somando as receitas e subtraindo as despesas. O saldo é mostrado ao usuário.

- **`filtrar_transacoes()`**  
  Possibilita filtrar as transações de acordo com o tipo (receita/despesa) ou a categoria definida pelo usuário. As transações filtradas são exibidas de acordo com os critérios escolhidos.

- **`exportar_csv()`**  
  Gera um arquivo CSV com todas as transações registradas. O nome do arquivo é fornecido pelo usuário no momento da exportação. As transações exportadas são específicas para o usuário logado.

### 🧭 **Menu Interno**

- **`menu_interno()`**  
  Apresenta as opções disponíveis após o login: adicionar transações, listar transações, consultar o saldo, aplicar filtros ou exportar os dados para CSV. O menu permanece em execução até que o usuário opte por sair.

### 🏠 **Menu Principal**

- O menu principal oferece as opções de cadastro, login ou sair do sistema. Ele funciona em loop, permitindo múltiplas interações com o usuário até que uma opção seja escolhida.

---

## ✅ **Resumo Geral das Funcionalidades**

- ✅ **Cadastro e autenticação de usuários**  
  O sistema permite que usuários se cadastrem e realizem login, com verificação de duplicidade de nomes.

- ✅ **Registro de transações financeiras (receitas e despesas)**  
  O sistema permite adicionar transações, organizando-as por tipo (receita/despesa), categoria e valor.

- ✅ **Visualização de todas as transações realizadas**  
  O usuário pode listar todas as suas transações registradas, com detalhes sobre cada uma delas.

- ✅ **Cálculo do saldo atual com base nas movimentações**  
  O saldo é atualizado conforme novas transações são adicionadas.

- ✅ **Filtro de transações por tipo ou categoria**  
  Permite que o usuário filtre as transações registradas, facilitando a visualização de determinadas categorias ou tipos de movimentação.

- ✅ **Exportação dos dados financeiros para um arquivo CSV**  
  O sistema permite exportar as transações para um arquivo CSV, facilitando o backup ou análise dos dados.

- ✅ **Navegação simples e interativa através de menus**  
  O programa possui menus intuitivos para facilitar a interação com o usuário.

---

## 📁 **Estrutura de Arquivos**

- **`usuarios.txt`**  
  Armazena os nomes de usuários e suas respectivas senhas. Cada linha contém o nome do usuário e a senha separados por vírgula.

- **`transacoes_<usuario>.csv`**  
  Arquivo CSV onde são armazenadas as transações de cada usuário. O nome do arquivo é gerado automaticamente com base no nome do usuário (ex: `transacoes_jose.csv`).

---

## 🛠️ **Como Usar**

1. **Iniciar o Programa**  
   - Execute o programa. O menu principal será exibido.

2. **Cadastrar Usuário**  
   - Escolha a opção para cadastrar um novo usuário e forneça um nome de usuário e senha.
   - Se o nome de usuário já estiver cadastrado, o sistema exibirá uma mensagem informando que o nome está em uso.

3. **Fazer Login**  
   - Escolha a opção para fazer login e forneça o nome de usuário e a senha.
   - Após o login bem-sucedido, o menu de transações será exibido, com opções para adicionar, listar e exportar transações, entre outras.

4. **Adicionar Transações**  
   - No menu de transações, você pode adicionar receitas ou despesas, detalhando categoria e valor.

5. **Filtrar e Exportar Transações**  
   - Você pode filtrar transações por tipo ou categoria.
   - Também pode exportar suas transações para um arquivo CSV.

6. **Ver Saldo**  
   - O sistema calcula e exibe o saldo atual, baseado nas transações registradas.

---

## 🖥️ **Como Executar o Programa**

1. Clone ou baixe o repositório para o seu computador.
2. Certifique-se de ter o Python 3.x instalado.
3. Execute o programa via terminal ou prompt de comando:
   ```bash
   python controle_financeiro.py
   ```

---

## ⚙️ **Exemplos de Uso**

### Cadastro de Usuário

```plaintext
============= Cadastro de Usuário =============
Digite o nome de usuário: jose
Digite a senha: 12345
Usuário cadastrado com sucesso!
```

### Login de Usuário

```plaintext
============= Login =============
Digite o nome de usuário: jose
Digite a senha: 12345
Login bem-sucedido! Bem-vindo, jose!
```

### Adicionar Transação

```plaintext
Digite o tipo (receita/despesa): receita
Digite a categoria (ex: alimentação, transporte): salário
Digite o valor: 1500
Transação registrada com sucesso!
```

### Listar Transações

```plaintext
=== Lista de Transações ===
1. Tipo: Receita, Categoria: Salário, Valor: R$ 1500.00
```

### Ver Saldo

```plaintext
Saldo atual: R$ 1500.00
```

### Exportar para CSV

```plaintext
Digite o nome do arquivo (ex: relatorio.csv): relatorio_jose.csv
Transações exportadas com sucesso para 'relatorio_jose.csv'!
```
---
