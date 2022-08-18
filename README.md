# orientacao-de-objeto-alura
projeto de estudo de orientação de objeto em python pela plataforma Alura
                O QUE É:

  Codigo referente ao projeto de estudos na plataforma Alura de educação.

  O objetivo do curso era aprender sobre a criação e uso de classes e objetos.
  
  codigo escrito por mim durante o processo de ensino, com algumas modificações pessoais feitas apos a conclusão do curso (ver adendo no final do READ ME), mas com credito ao professor pela orientação.
  
  Projeto refere-se a contrução de um sitema de contas bancarias e suas propriedades para o aprendizado de orientação de objetos em python.
  
  Agradecimento ao Prof. Nico Steppat

                DESCRIÇÃO:

  o sitema de contas de um banco ficticio é simples para a identificação de caracteristicas atribuidas a clientes ficticios como nome do titular, saldo, conta, agencia, etc...
  
                METODOS DISPONIVEIS NO PROGRAMA:

  - metodo estatico com o codigo do banco ficticio que determinei como "000"
  - extrato
  - transferencia (com consideração de limite)
  - saque (com consideração de limite)
  - deposito)
  - alteração de limite (com o uso de @property)

                OPÇOES ADICIONADAS APOS O CURSO

  apos encerrar o curso de orientação de dados com o prof. Nico, decidi adicionar ao programa diferentes especificações de conta e novos métodos para optimizar a experiencia de um possivel usuario.
  meu primeiro passo foi importar a biblioteca math do python. depois adicionar a possibilidade de diferente tipos de conta (conta corrente, salario, porlpança) utilizando a classe Conta original como uma classe-mae.
  importante considerar o que os tres tipos de conta inseridos tem de diferencial:

      - conta corrente:
   > conta que disponibiliza facil acesso aos recursos depositados.
   > metodo facil de movimentação de dinheiro
   > opção de cartão de credito (parcelamento de contas)
   > possibilidade de transferencia bancaria
   > sem possibilidade de obter rendimento

      - polpança:
   > cardeneta administrada pelo banco para investimentos
   > aplicação de recursos para rendimento
   > sem possibilidade de saque antes de tempo determinado
   > rendimento em porcentagem a juros simples
   > com possibilidade de receber transferencia, mas não de fazer antes do tempo determinado
   
      - conta salario
   > é uma conta aberta por iniciativa e solicitação do empregador para efetuar o pagamento de salários aos seus empregados
   > apenas recebe depositos do empregador
   > permite saque, mas deposito apenas de uma fonte

  depois de terminar o que cada tipo de conta tem posso adicionar os metodos unicos de cada e bloquear os methos da conta mae que não se aplicam

                OUTROS METODOS DISPONIVEIS NO PROGRAMA:

- metodo para redefinir a quantidade de parcelas pernmitidas pelo banco
- checagem se o pagamento pode ser efetuado considerando o limite da conta
- para a redeterminação das parcelas
- determinação do valor de cada parcela
- checagem da disponibilidade de retirada da polpança
- saque e transferencia levando em consideração a disponibilidade
- definição de lucro e montante da polpança
- para a modificação do periodo
- para a modificação do juros
- para o deposito ser feito apenas pelo contratante

                AGRADECIMENTO
Obrigado pela atenção.
gostaria de agradecer ao prof. Nico e a plataforma Alura tambem
