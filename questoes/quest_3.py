import json

caminho_arquivo = '../dados.json'

with open(caminho_arquivo) as arquivo:
    dados = json.load(arquivo)

print(dados[0].get('valor'))

valores = []
for dado in dados:
    if dado.get('valor') != 0.0:
        valores.append([dado.get('dia'), dado.get('valor')])

valores.sort(key=lambda x: x[1])

print(f'O menor faturamento foi de R${valores[0][1]} no dia {valores[0][0]}.')
print(f'O maior faturamento foi de R${valores[-1][1]} no dia {valores[-1][0]}.')

media = sum([valor[1] for valor in valores]) / len(valores)

dias_acima_media = 0
for valor in valores:
    if valor[1] > media:
        dias_acima_media += 1

print(f'{dias_acima_media} dias tiveram o valor de faturamento diário superior à média mensal.')