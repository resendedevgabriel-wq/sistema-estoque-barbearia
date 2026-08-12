estoque = [
    { "nome": "Creme Modelador", "quantidade": 10,"preco": 25.0},
    { "nomme": "Shampoo", "quantidade": 5, "preco": 20.0},
    { "nome": "Pomada", "quantidade": 2, "preco": 10.0},
    { "nome": "Hidratante", "quantidade": 15, "preco": 39},
    { "nome": "Pente", "quantidade": 10, "preco": 22},
    { "nome": "Oleo para Penteado", "quantidade": 4, "preco": 80},
]
custo_total_reposiçao = 0

for produto in estoque:
    if produto["quantidade"] < 5:
        faltam = 5 - produto["quantidade"]
        print(f"ALERTA: {produto['nome']} precisa de +{faltam} un. para atingir o minimo seguro! Atualmente ({produto['quantidade']} un.)")
        custo_total_reposiçao += faltam * produto["preco"]

print (f"Custo total estimado para reposiçao minima!: R$ {custo_total_reposiçao}")







