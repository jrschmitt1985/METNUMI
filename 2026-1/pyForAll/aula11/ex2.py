despesas_mensais = [
    ("aluguel", 1000),
    ("faculdade", 1500),
    ("aluguel", 1000),
    ("internet", 1400),
    ("condominio", 1100),
    ("internet", 1400)
]

categorias_unicas = set()
total_por_categoria = {}

for despesa, valor in despesas_mensais:
    categorias_unicas.add(despesa)
    total_por_categoria [despesa] = total_por_categoria.get(despesa, 0) + valor
for categoria, total in total_por_categoria.items():
    print(f"Total gasto com {categoria}:", 'R$ ', total)