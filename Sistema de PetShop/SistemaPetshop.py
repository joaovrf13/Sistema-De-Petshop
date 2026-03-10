from Funcoes import Exibir_Menu, Cadastrar_Clientes, Cadastrar_Pets, Listar_Clientes, Listar_Pets,Cadastar_Servicos,Relatorio

Exibir_Menu()

while True:
 opcao = input("Digite uma opção: ")
 if opcao == '1':
     Cadastrar_Clientes()
     Exibir_Menu()
 elif opcao == '2':
     Cadastrar_Pets()
     Exibir_Menu()
 elif opcao == '3':
    Listar_Clientes()
    Exibir_Menu()
 elif opcao == '4':
    Listar_Pets()
    Exibir_Menu()
 elif opcao == '5':
     Cadastar_Servicos()
     Exibir_Menu()
 elif opcao == '6':
     Relatorio()
     Exibir_Menu()
 elif opcao == '8':
     print("Saindo do Programa...")
     break
 else:
     print("Opção Invalida")