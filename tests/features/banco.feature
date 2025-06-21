Feature: Aplicação web para banco
  Obter e atualizar contas de clientes

  Como um cliente eu quero ser capaz de visualizar o meu saldo
  e atualizar o saldo
  e sacar um valor do saldo

  Scenario: Obter o saldo das contas.
    Given visito o app do banco.
    When entro com o número da conta "111".
    Then obtenho saldo == 50.
