#tabela FIPE com valores dos veiculos ficticios
tabela_fipe = {
    "Fusca": 25000,
    "Gol": 40000,
    "Jetta": 80000,
    "Polo": 55000,
    "Tiguan": 120000,
    "Civic": 80000,
    "Fit": 70000,
    "HR-V": 85000,
    "Accord": 100000,
    "CR-V": 110000,
    "Corolla": 90000,
    "Hilux": 150000,
    "Etios": 60000,
    "RAV4": 130000,
    "Camry": 140000,
    "Onix": 50000,
    "Tracker": 95000,
    "Cruze": 75000,
    "S10": 120000,
    "Montana": 45000,
    "HB20": 45000,
    "Creta": 100000,
    "i30": 65000,
    "Tucson": 110000,
    "Santa Fe": 150000
}

#listas de marcas e seus modelos
marcas = ["Volkswagen", "Honda", "Toyota", "Chevrolet", "Hyundai"]
modelos = [
    ["Fusca", "Gol", "Jetta", "Polo", "Tiguan"],
    ["Civic", "Fit", "HR-V", "Accord", "CR-V"],
    ["Corolla", "Hilux", "Etios", "RAV4", "Camry"],
    ["Onix", "Tracker", "Cruze", "S10", "Montana"],
    ["HB20", "Creta", "i30", "Tucson", "Santa Fe"]
]

#lista de veiculos disponiveis para aluguel e compra
veiculos_disponiveis = list(tabela_fipe)

#obter informações do cliente
print("-----Cadastro do Cliente-----")
nome = input("Informe seu nome: ")
telefone = input("Informe seu telefone: ")
saldo = float(input("Informe seu saldo disponível: R$ "))
print("\nBem-vindo, {}! Seu saldo inicial é R$ {:.2f}.".format(nome, saldo))

#menu principal
while True:
    print("\n--- Bem-vindo ao Sistema de Compra, Venda e Aluguel de Veículos ---")
    print("1. Vender veículo")
    print("2. Alugar veículo")
    print("3. Comprar veículo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    #vender veiculo
    if opcao == '1': 
        print("\nMarcas disponíveis para venda:")
        i = 0
        while i < len(marcas):
            print("{}. {}".format(i + 1, marcas[i]))
            i += 1
        
        marca_escolhida = int(input("Escolha uma marca (1-5): "))
        if marca_escolhida < 1 or marca_escolhida > len(marcas):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(marcas)))
            continue
        
        marca_selecionada = marcas[marca_escolhida - 1]
        
        print("\nModelos disponíveis da marca {}:".format(marca_selecionada))
        modelo_lista = modelos[marca_escolhida - 1]
        i = 0
        while i < len(modelo_lista):
            print("{}. {}".format(i + 1, modelo_lista[i]))
            i += 1
        
        modelo_escolhido = int(input("Informe o modelo do veículo que deseja vender (1-5): "))
        if modelo_escolhido < 1 or modelo_escolhido > len(modelo_lista):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(modelo_lista)))
            continue
        
        modelo_selecionado = modelo_lista[modelo_escolhido - 1]
        
        if modelo_selecionado in tabela_fipe:
            valor_avaliado = tabela_fipe[modelo_selecionado]
            proposta = valor_avaliado * 0.88  
            aceitar = input("A proposta é de R$ {:.2f}. Deseja continuar? (s/n): ".format(proposta))
            
            if aceitar.lower() == 's':
                saldo += proposta
                veiculos_disponiveis.append(modelo_selecionado)  
                print("Veículo {} vendido com sucesso! Seu novo saldo é R$ {:.2f}.".format(modelo_selecionado, saldo))
            else:
                print("Venda cancelada.")
        else:
            print("Modelo não encontrado na tabela FIPE.")
    
    #alugar veiculo
    elif opcao == '2': 
        print("\nMarcas disponíveis para aluguel:")
        i = 0
        while i < len(marcas):
            print("{}. {}".format(i + 1, marcas[i]))
            i += 1
        
        marca_escolhida = int(input("Escolha uma marca (1-5): "))
        if marca_escolhida < 1 or marca_escolhida > len(marcas):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(marcas)))
            continue
        
        marca_selecionada = marcas[marca_escolhida - 1]
        
        print("\nModelos disponíveis da marca {}:".format(marca_selecionada))
        modelo_lista = modelos[marca_escolhida - 1]
        i = 0
        while i < len(modelo_lista):
            if modelo_lista[i] in veiculos_disponiveis:  
                print("{}. {}".format(i + 1, modelo_lista[i]))
            i += 1
        
        modelo_escolhido = int(input("Escolha um veículo para alugar (1-5): "))
        if modelo_escolhido < 1 or modelo_escolhido > len(modelo_lista):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(modelo_lista)))
            continue
        
        modelo_selecionado = modelo_lista[modelo_escolhido - 1]
        
        if modelo_selecionado in veiculos_disponiveis:
            dias = int(input("Informe o número de dias desejados: "))
            custo_total = dias * 77
            
            print("O custo total para alugar {} por {} dias é R$ {:.2f}.".format(modelo_selecionado, dias, custo_total))
            
            confirmar = input("Deseja prosseguir com o aluguel? (s/n): ")
            
            if confirmar.lower() == 's':
                if saldo >= custo_total:
                    saldo -= custo_total
                    veiculos_disponiveis.remove(modelo_selecionado)  
                    print("Veículo {} foi alugado com sucesso! Seu novo saldo é R$ {:.2f}.".format(modelo_selecionado, saldo))
                else:
                    print("Saldo insuficiente para aluguel.")
            elif confirmar == '0':
                print("Aluguel cancelado.")
            else:
                print("Operação cancelada.")
        else:
            print("Veículo não disponível.")
    
    #comprar veiculo
    elif opcao == '3': 
        print("\nMarcas disponíveis para compra:")
        i = 0
        while i < len(marcas):
            print("{}. {}".format(i + 1, marcas[i]))
            i += 1
        
        marca_escolhida = int(input("Escolha uma marca (1-5): "))
        if marca_escolhida < 1 or marca_escolhida > len(marcas):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(marcas)))
            continue
        
        marca_selecionada = marcas[marca_escolhida - 1]
        
        print("\nModelos disponíveis da marca {}:".format(marca_selecionada))
        modelo_lista = modelos[marca_escolhida - 1]
        i = 0
        while i < len(modelo_lista):
            if modelo_lista[i] in veiculos_disponiveis:  
                print("{}. {}".format(i + 1, modelo_lista[i]))
            i += 1
        
        modelo_escolhido = int(input("Escolha um veículo para comprar (1-5): "))
        if modelo_escolhido < 1 or modelo_escolhido > len(modelo_lista):
            print("Opção inválida! Por favor, escolha um número entre 1 e {}.".format(len(modelo_lista)))
            continue
        
        modelo_selecionado = modelo_lista[modelo_escolhido - 1]
        
        if modelo_selecionado in veiculos_disponiveis and modelo_selecionado in tabela_fipe:
            valor_avaliado = tabela_fipe[modelo_selecionado]
            preco_final = valor_avaliado * 1.25  
            
            #exibir preços
            print("\nPreço na Tabela FIPE: R$ {:.2f}".format(valor_avaliado))
            print("Preço total com acréscimo de venda: R$ {:.2f}".format(preco_final))
            
            confirmar_compra = input("Deseja continuar com a compra? (s/n): ")
            
            if confirmar_compra.lower() == 's':
                if saldo >= preco_final:
                    saldo -= preco_final
                    veiculos_disponiveis.remove(modelo_selecionado)  
                    print("A compra do veículo {} foi feita com sucesso! Seu novo saldo é R$ {:.2f}.".format(modelo_selecionado, saldo))                
                    
                else:
                    print("Saldo insuficiente para compra.")
            else:
                print("Compra cancelada.")
                
        else:
            print("Modelo não disponível ou não encontrado na tabela FIPE.")
    
    #sair do sistema
    elif opcao == '4':  
        print("Saindo do sistema. Até logo!")
        break
    
    #opção invalida
    else:
        print("Opção inválida! Tente novamente.")