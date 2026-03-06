Clientes = []
Pets = []
Servicos = []

def Cadastrar_Clientes():
 Nome = input("Digite seu nome: ")
 Documento = input("Digite seu documento: ")
 Telefone = input("Digite seu telefone: ")
 Endereco = input("Digite seu endereço: ")

 Cliente = {
   "Nome" : Nome,
   "Documento" : Documento,
   "Telefone": Telefone,
   "Endereco": Endereco
 }

 Clientes.append(Cliente)


def Cadastrar_Pets():
    NomePet = input("Digite o nome do pet: ")
    Raca = input("Digite a raça do seu pet: ")
    Sexo = input("Digite o sexo: ")
    DocumentoDono = input("Digite o documento do dono: ")

    Pet = {
     "NomePet" : NomePet,
     "Raca" : Raca,
     "Sexo" : Sexo,
     "DocumentoDono" : DocumentoDono
    }
    Pets.append(Pet)

 
def Listar_Clientes():
  print("== Clientes Cadastrados ==")
  for Cliente in Clientes:
    print("Nome: ", Cliente["Nome"])
    print("Documento: ", Cliente["Documento"])
    print("Telefone: ", Cliente["Telefone"])
    print("Endereço: ", Cliente["Endereco"])

def Listar_Pets():
  print("== Pets Cadastrados ==")
  for Pet in Pets:
   print("Nome: ", Pet["Nome"])
   print("Raca: ", Pet["Raca"])
   print("Sexo: ", Pet["Sexo"])


def Cadastar_Servicos():
 print("== Serviços ==")
 print("1 - Banho: R$ 80 ")
 print("2 - Tosa: R$ 100 ")
 print("3 - Consulta: R$ 120 ")
 print("4 - Hospedagem: R$ 150 ")
 
 Servicos_Disponiveis = {
      1:{'nome': 'Banho','preco': 80},
      2:{'nome': 'Tosa','preco': 100},
      3:{'nome': 'Consulta','preco': 120},
      4:{'nome': 'Hospedagem','preco': 150},
    }
 
 while True:
   OpcaoServico = int(input("Selecione um serviço: "))
   if OpcaoServico in Servicos_Disponiveis:
    servico = Servicos_Disponiveis[OpcaoServico]
    Servicos.append(servico)
    break
   else:
    print("Serviço Indisponivel")


  

 


def Exibir_Menu():
 print("== SISTEMA PETSHOP ==")
 print("1 - Cadastrar Cliente")
 print("2 - Casdastrar Pet")
 print("3 - Listar Clientes")
 print("4 - Listar pets")
 print("5 - Registrar serviço")
 print("6 - Exibir relatório")
 print("7 - Buscar pet")
 print("8 - Sair")
 



