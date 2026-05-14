contas_a_pagar = ["telefone", "faculdade", "aluguel", "internet", "condominio", "agua", "luz"]
contas_a_receber = ["salario", "aluguel", "bolsa", "freelas", "mesada"]

conjunto = set(contas_a_pagar)
conjunto_2 = set(contas_a_receber)

contas_em_comum = conjunto.intersection(conjunto_2)
print(contas_em_comum)
contas_diferentes = conjunto.difference(conjunto_2)
print(contas_diferentes)
contas_diferentes_2 = conjunto_2.difference(conjunto)
print(contas_diferentes_2)
contas_unicas = conjunto.union(conjunto_2)
print(contas_unicas)
