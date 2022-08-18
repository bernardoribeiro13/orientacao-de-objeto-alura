#criação da classe-mae para definir o que todos os tipos de conta tem em comum
class Conta:
  def __init__(self, conta, agencia, titular, saldo, limite):
    print("criando conta: {}".format(self))
    self.self = self
    self._conta = conta
    self._agencia = agencia
    self._titular = titular
    self._saldo = saldo
    self._limite = limite

#codigo do codigo do banco ficticio a quem todas as contas pertencem
    
  @staticmethod
  def codigo_banco():
    return "000"

#metodos disponiveis na conta-mae e consequente nas filhas
#possibiliade de extratos com a impressão do saldo bancario e do limite da conta
#extrato por enquanto apenas com o saldo e limite


  def extrato(self):
    print("O saldo da conta {} é {}".format(self._conta, self._saldo))
    print("O limite da conta {} é {}".format(self._conta, self._limite))

#metodo de deposito bancario com o uso de valor para somar com o saldo atual, modificando o saldo original
 
  
  def deposito(self, valor):
    self._saldo += valor
    print("saldo atual da conta {}: {}".format(self._conta, self._saldo))

#metodo de disponibilidade somando o limite e o saldo, para uma checagem interna para o uso em outros metodos
#esse metodo encontra-se trancado para ediçoes futuras com o objetivo de ser apenas uma consideração para o projeto e não para o usuario
  
  def __disponibilidade(self, valor_requerido):
    valor_disponivel = self._saldo + self._limite
    return valor_requerido <= valor_disponivel

#metodos de saque e transferencia utilizando o metodo de __disponibilidade para considerarem o limite disponivel para a conta
  
  def saque(self, valor):
    if self.__disponibilidade(valor) == True:
       self._saldo -= valor
       print("saldo atual da conta {}: {}".format(self._conta, self._saldo))
    else:
      print("sinto muito, valor ultrapassa limite da conta")

  def transferencia(self, valor, destino):
    if self.__disponibilidade(valor) == True:
      self.saque(valor)
      destino.deposito(valor)
    else:
      print("sinto muito, valor ultrapassa limite da conta")

#metodos genericos para alcançar os dados disponiveis internamente
  
  def get_saldo(self):
    return self._saldo()

  def get_titular(self):
    return self._titular

  def get_conta(self):
    return self._conta

  def get_agencia(self):
    return self._agencia

  @property
  def limite(self):
    return self._limite

  @limite.setter
  def limite(self, limite):
    self._limite = limite

#criação dos tipos de conta, todas como classes-filhas da classe-mãe Conta
#conta corrente. diferencial: parcelamento de compras

class ContaCorrente(Conta):
  def __init__(self, conta, agencia, titular, saldo, limite):
    self.parcelas = int(10)
    super().__init__(conta, agencia, titular, saldo, limite)

#conta corrente tem que ter o metodo para parcelar as compras e aumento de parcelas possiveis
 
  def parcelas_alterar(self):
    tipo = input(f"voce deseja aumentar ou diminur o numero de parcelas da conta {self._conta}? ")
    numero_adicional = int(input(f"quantas parcelas voce deseja {tipo} à conta {self._conta}? "))
    if tipo == "aumentar":
      self.parcelas += numero_adicional
      print(f"Parcelas agora são {self.parcelas}")
    elif tipo == "diminuir":
      self.parcelas -= numero_adicional
      print(f"Parcelas agora são {self.parcelas}")
    else:
      print("não entendi seu requerimento, por favor tente de novo")

#tambem precisa que o valor a ser parcelado não seja maior que o limite
#uso de variavel interna para a consideração do limite no ato de pagamentos

  def __disponibilidade(self, valor_requerido):
    valor_disponivel = self._saldo + self._limite
    return valor_requerido <= valor_disponivel

  def pagamento(self, valor_requerido):
    if self.__disponibilidade == True:
      print(f"sinto muito, mas {valor_requerido} ultrapassa {self._limite}")
    else:
      self._saldo -= valor_requerido
      print("pagamento efetuado")  
      print(f"Seu saldo agora é {self._saldo}")

#metodo para saber quanto é a parcela

  def valor_parcela(self, total):
    print(f"total dividido em {self.parcelas} parcelas de {int(total)/int(self.parcelas)}")
    
class Polpança(Conta):
  def __init__(self, conta, agencia, titular, saldo, limite, juros, periodo):
    self._juros = juros
    self.periodo = periodo
    self.__ganho = int(0)
    super().__init__(conta, agencia, titular, saldo, limite)
 
#introdução de methodos exclusivos a polpança
#é preciso bloquear o saque e transferencia da polpança ate certo periodo

  def __disponibilidade(self, tempo):
    if tempo >= self.periodo:
      True
    else:
      False

  def saque(self, tempo, valor):
    if self.__disponibilidade(tempo) == True:
       self._saldo -= valor
       print("saldo atual da conta {}: {}".format(self._conta, self._saldo))
    else:
      print(f"sinto muito, saques ainda não disponiveis para conta {self._conta}")

  def transferencia(self, tempo, valor, destino):
    if self.__disponibilidade(tempo) == True:
      self.saque(valor)
      destino.deposito(valor)
    else:
      print(f"sinto muito, sinto muito transferencias ainda não disponiveis para conta {self._conta}")

#agora calcular o ganho da conta durante o tempo de uso da conta

  def ganho(self):
    lucro = float(self._juros)*float(self._saldo)
    return lucro


  def montante(self, tempo):
    montante = float(self._juros)*float(self._saldo)*tempo
    return montante

#metodo para a modificação do juros
  
  def juros(self, modificação):
    tipo = input(f"voce deseja aumentar ou diminur o juros da conta {self._conta}? ")
    if tipo == "aumentar":
      self._juros += modificação
      print(f"juros modificado para {self._juros}")
    elif tipo == "diminur":
      self.juros += modificação
    else:
      print("não entendi seu requerimento, por favor tente de novo")

class ContaSalario(Conta):
  def __init__(self, conta, agencia, titular, saldo, limite, empresa):
    self.empresa = empresa
    super().__init__(conta, agencia, titular, saldo, limite)

#a principal caracteristica da conta salario é que apenas o empregador pode depositar

  def deposito(self, conta_remetente, valor):
    if conta_remetente._titular == self.empresa:
      self._saldo += valor
      print("saldo atual da conta {}: {}".format(self._conta, self._saldo))
    else:
        print("sinto muito, apenas o empregador pode depositar nessa conta")
      
#outros metodos podem ser copiados da classe mae

conta1 = ContaCorrente(1, 1, "Guillermo de la Cruz", 1200.0, 2000.0)

conta2 = ContaSalario(2, 1, "Jonathan Sims", 0.5, 1200.0, "Magnus Institute")

conta3 = Polpança(3, 1, "Martin Blackwood", 100.0, 0, 0.01, 12)

conta4 = ContaCorrente(4, 1, "Elias Bouchard", 100000.00, 100000.00)

conta5 = Polpança(5, 1, "Georgie Baker", 5000,0, 0.01, 5)

conta6 = ContaSalario(6, 1, "Presenter", 3000, 3000, "Comunity Radio for  the Liminal comunity")

conta7 = ContaCorrente(7, 1, "Samael Apollo Einfield", 200.0, 1200)

conta8 = Polpança(8, 1, "Oliver Boleyn", 30000.0, 0, 00.5, 6)

conta9 = ContaSalario(9, 1, "Peter Lukas", 100000.00, 100000.00, "Lukas Transportation")
 
conta10 = ContaCorrente(10, 1, "Ashton Greymoor", 0.5, 100.0)

conta11 = ContaSalario(11, 2, "Percival de Rolo", 3000, 3000, "Whitestone")

conta12 = Polpança(12, 2, "Vex de Rolo", 5000, 0, 0.06, 24)

conta13 = ContaCorrente(13, 2, "Magnus Institute", 100000.00, 100000.00)