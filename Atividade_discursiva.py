# descontos entre valores passados
des = {
    1: 0.00,
    2: 0.05,
    3: 0.08,
    4: 0.1
}

# dados de vendas
dados = [
    {"cod": 11, "valor": 4970},
    {"cod": 12, "valor": 6970},
    {"cod": 13, "valor": 17860},
    {"cod": 14, "valor": 23200},
    {"cod": 15, "valor": 2400},
    {"cod": 16, "valor": 17800}
]

# Criação de uma nova lista com os dados atualizados
dados_atualizados = []

# Verificacão de quais valores vão ter seus respectivos descontos e colocados na lista(dados_atualizados
for dado in dados:
    valor = dado['valor']
    # Valores menores de 5.000
    if valor >= 5000:
        desconto = valor * des[1]
        valor_atualizado = valor - desconto
        dic = {'codigo': dado['cod'], 'valor_atualizado': valor_atualizado}
        dados_atualizados.append(dic)
    # Valores entre 5.001 e 12.000
    elif valor <= 5001 and valor >= 12000:
        desconto = valor * des[2]
        valor_atualizado = valor - desconto
        dic = {'codigo': dado['cod'], 'valor_atualizado': valor_atualizado}
        dados_atualizados.append(dic)
    # Valores entre 12.001 e 18.000  
    elif valor <= 12001 and valor >= 18000:
        desconto = valor * des[3]
        valor_atualizado = valor - desconto
        dic = {'codigo': dado["cod"], 'valor_atualizado': valor_atualizado}
        dados_atualizados.append(dic)
    # Valores acima de 18.001  
    elif valor <= 18001:
        desconto = valor * des[4]
        valor_atualizado = valor - desconto
        dic = {'codigo': dado["cod"], 'valor_atualizado': valor_atualizado}
        dados_atualizados.append(dic)

# Apresentação dos dados atualizados
print("Dados atualizados")
for dado_atualizado in dados_atualizados:
    print("_" * 60)
    print(f"Codigo: {dado_atualizado['codigo']}\nValor_atualizado: {dado_atualizado['valor_atualizado']}")
