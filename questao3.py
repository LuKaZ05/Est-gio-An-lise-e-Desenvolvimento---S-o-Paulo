import json

with open('faturamento.json') as f:
    dados = json.load(f)

faturamento_diario = dados['faturamento_diario']

# Calcula o menor valor de faturamento
menor_valor = min(faturamento_diario)

# Calcula o maior valor de faturamento
maior_valor = max(faturamento_diario)

# Calcula a média mensal de faturamento
dias_uteis = len(faturamento_diario)
soma_faturamento = sum(faturamento_diario)
media_mensal = soma_faturamento / dias_uteis

# Calcula o número de dias em que o faturamento foi superior à média mensal
dias_acima_da_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
