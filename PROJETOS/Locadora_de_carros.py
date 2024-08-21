import os

carros_estoque = {
     0 : "Chevrolet Tracker - R$ 120 / dia",
     1 : "Chevrolet Onix - R$ 90 / dia",
     2 : "Chevrolet Spin - R$ 150 / dia",
     3 : "Hyundai HB20 - R$ 85 / dia",
     4 : "Hyundai Tucson - R$ 120 / dia",
     5 : "Fiat Uno - R$ 60 / dia",
     6 : "Fiat Mobi - R$ 70 / dia",
     7 : "Fiat Pulse - R$ 130 / dia"
    }
carros_alugados = {
}
while True:
    os.system("cls")
    
    print("=============")
    print("Bem vindo à locadora de carros!")
    print("=============")
    print("O que deseja fazer?")
    print("")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    
    acao = int(input())
    
    if acao == 0:
        for i, carro in carros_estoque.items():
            print("[{}]".format(i), carro)
        print()
        print()
        print()
        print("=============")
        print("0 - CONTINUAR | 1 - SAIR")
        acao_portfolio = int(input())
        if acao_portfolio == 0:
            pass
        elif acao_portfolio == 1:
            break
    elif acao == 1:
        for i, carro in carros_estoque.items():
            print("[{}]".format(i), carro)
        print()
        print()

        print("=============")
        print("Escolha o código do carro:")
        modelo = int(input())
            
        print("Diga por quantos dias:")
        dias = int(input())
        
        if modelo == 0:
            result = dias * 120
        elif modelo == 1:
            result = dias * 90
        elif modelo == 2:
            result = dias * 150
        elif modelo == 3:
            result = dias * 85
        elif modelo == 4:
            result = dias * 120
        elif modelo == 5:
            result = dias * 60
        elif modelo == 6:
            result = dias * 70
        elif modelo == 7:
            result = dias * 130
            
        print("Você escolheu {} por {} dias.".format(carros_estoque[modelo].split(" -")[0], dias))
        print("O aluguel vai custar R$ {}. Deseja alugar?".format(result))
        print()
        print("0 - SIM | 1 - NÃO")
        acao_locacao = int(input())
        
        if acao_locacao == 0:
            print("Você alugou o {} por {} dias.".format(carros_estoque[modelo].split(" -")[0], dias))
            carros_alugados[modelo] = carros_estoque[modelo]
            del carros_estoque[modelo]
            
            print()
            print("=============")
            print("0 - CONTINUAR | 1 - SAIR")
            acao_portfolio = int(input())
            
            if acao_portfolio == 0:
                pass
            elif acao_portfolio == 1:
                break
        else:
            pass
    elif acao == 2:
        print("Segue a lista de carros alugados, qual você deseja devolver?")
        for i, carro in carros_alugados.items():
            print("[{}]".format(i), carro)
        print()
        print()
        print()
        print("Escolha o código do carro que deseja devolver:")

        modelo = int(input())
        
        carros_estoque[modelo] = carros_alugados[modelo]
        del carros_alugados[modelo]
        
        print("Obrigado por devolver o carro {}".format(carros_estoque[modelo].split(" -")[0]))
        print("=============")
        print("0 - CONTINUAR | 1 - SAIR")
        acao_portfolio = int(input())
        if acao_portfolio == 0:
            pass
        elif acao_portfolio == 1:
            break
