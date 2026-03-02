Clientes = []
Pets = []


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

    Pet = {
      "NomePet" : NomePet,
      "Raca" : Raca,
      "Sexo" :Sexo  
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

