# Preços Fixos
DOLAR_COTADO = 5.16
PRECO_IOF_CARTOES = 0.35

# Dicionário de ICMS
IMPOSTOS_ESTADOS = {
    "SP": 0.18,
    "MG": 0.18,
    "RJ": 0.22,
    "SC": 0.17
    
}

# Menu Principal
while (True):
        print("SISTEMAS DE CALCULO PARA PRODUTOS FINAL - DANIEL G.")
        print( "\n" + "=" * 30)
        print("\n1- Acessar Calculadora de Preços finais Básica | \n2- Acessar Calculadora Inter Estadual de preços finais | 3- Sair")
        entrada_dados = input("\nDigite o número do que deseja fazer: ")
    
        if entrada_dados == "3":
            print("ENCERRANDO O PROGRAMA...")
            break
        
        elif entrada_dados == "1":
                print("\n--- Calculadora básica de preço final do consumidor--- ")
                preco_base = input("\nDigite o preço base do produto: ")
                preco_base_conv = float(preco_base)
                imposto_fixo = 0.35 * preco_base_conv
                margem_lucro = 0.10 * (preco_base_conv + imposto_fixo)
                valor_final = preco_base_conv + imposto_fixo + margem_lucro
                print(f"\nPreço de venda final do produto: {valor_final:.2f}")
                pass
        
        elif entrada_dados == "2":
            print("\n--- Calculadora Inter Estadual para Preços finais--- ")
            
            estado = input("Digite o seu estado: ").upper()
            if estado in IMPOSTOS_ESTADOS:
                taxa = IMPOSTOS_ESTADOS[estado]
                cotacao_input = input("Digite a cotação do Dólar hoje: ")
                cotacao_atual = float(cotacao_input)
                preco_base = input("\nDigite o preço base do produto: ")
                preco_base_conv = float(preco_base)
                
                preco_reais = preco_base_conv * cotacao_atual
                valor_com_iof = preco_reais * (1 + PRECO_IOF_CARTOES)
                valor_final = valor_com_iof * (1 + taxa)
                
                print(f"O valor estimado do GTA VI em {estado} é: R$ {valor_final:.2f}")
                pass
            else:
                print("Estado não encontrado na base de dados.")
        
else:
            print("Opção inválida! Tente novamente.")       