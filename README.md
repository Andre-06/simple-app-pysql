# Simple App - PySQL

Este projeto foi desenvolvido durante o curso "Desenvolvendo um Projeto Completo Python com Estruturas de Dados" oferecido pela Fundação Bradesco. O objetivo do aplicativo é gerenciar um banco de dados de clientes utilizando a linguagem Python e a biblioteca Tkinter para a interface gráfica.

## Funcionalidades

- **Visualizar Clientes**: Exibe todos os clientes cadastrados na base de dados.
- **Buscar Clientes**: Permite buscar clientes específicos com base nos critérios fornecidos (nome, sobrenome, e-mail, CPF).
- **Inserir Cliente**: Adiciona um novo cliente ao banco de dados.
- **Atualizar Cliente**: Atualiza as informações de um cliente selecionado.
- **Deletar Cliente**: Remove um ou mais clientes selecionados da base de dados.

## Instalação

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o aplicativo:
   ```bash
   python main.py
   ```

2. Utilize a interface gráfica para gerenciar os clientes do banco de dados:
   - Clique em "Ver Todos" para exibir todos os clientes cadastrados.
   - Use os campos de texto para buscar, inserir, atualizar ou deletar clientes.

## Estrutura do Projeto

- `main.py`: Arquivo principal para execução do aplicativo.
- `GUI.py`: Contém a definição da classe da interface gráfica do usuário utilizando Tkinter.
- `connector.py`: Contém as funções de conexão e manipulação do banco de dados SQLite.

## Contribuição

Sinta-se à vontade para fazer fork deste repositório, criar novas features ou corrigir bugs. Pull requests são bem-vindos!

## Agradecimentos

Este projeto foi desenvolvido durante o curso **"Desenvolvendo um Projeto Completo Python com Estruturas de Dados"** oferecido pela **Fundação Bradesco**. Agradecemos à instituição por proporcionar este excelente material educacional.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
