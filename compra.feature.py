Como cliente da EBAC-SHOP
Quero fazer concluir meu cadastro   
Para finalizar minha compra
Critérios de Aceitação:
1 – Deve ser cadastrado com todos os dados obrigatórios, marcado com asteriscos
2 – Não deve permitir campo e-mail com formato inválido. Sistema deve inserir uma mensagem de erro
3 – Ao tentar cadastrar com campos vazios, deve exibir mensagem de alerta. 
Funcionalidade: Cadastro de cliente
  Como cliente da EBAC-SHOP
  Quero me cadastrar corretamente na plataforma
  Para conseguir acessar e utilizar todas as funcionalidades da loja

  Cenário: Cadastro com todos os campos obrigatórios preenchidos corretamente
    Dado que estou na página de cadastro da EBAC-SHOP
    Quando eu preencher todos os campos obrigatórios marcados com asterisco
    E inserir um e-mail válido "usuario@exemplo.com"
    E clicar no botão "Cadastrar"
    Então o sistema deve concluir o cadastro com sucesso
    E exibir a mensagem "Cadastro realizado com sucesso"

  Cenário: Cadastro com e-mail em formato

Funcionalidade: Cadastro de cliente
  Como cliente da EBAC-SHOP
  Quero me cadastrar corretamente na plataforma
  Para acessar e utilizar as funcionalidades da loja

  Esquema do Cenário: Validação dos dados no formulário de cadastro
    Dado que estou na página de cadastro da EBAC-SHOP
    Quando eu preencher o nome com "<nome>"
    E preencher o e-mail com "<email>"
    E preencher a senha com "<senha>"
    E clicar no botão "Cadastrar"
    Então o sistema deve exibir a mensagem "<mensagem>"

Exemplos:
      | nome          | email                 | senha        | mensagem                             |
      | João Silva    | joao@email.com        | senha123     | Cadastro realizado com sucesso       |
      | Maria Souza   | mariaemail.com        | senha123     | Formato de e-mail inválido           |
      |               | maria@email.com       | senha123     | Por favor, preencha todos os campos  |
      | Ana Oliveira  | ana@email.com         |              | Por favor, preencha todos os campos  |
      |               |                       |              | Por favor, preencha todos os campos  |
