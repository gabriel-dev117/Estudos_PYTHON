# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produto por nome descrescente;
# Gere produtos_ordenados_por_nome por deep copy;

# Ordene os produtos por preço crescente;
# Gere produtos_ordenados_por_preco por deep copy

# ------------------------------------------------------------------

from dados import produtos
import copy

print("----------| Valor Original |----------")
print(*produtos, sep='\n')    

for produto in produtos:
    produto['valor'] = (produto['valor']) + (produto['valor'] * 0.1) 

produtos_atualizados = copy.deepcopy(produtos)

print("\n\n----------| Valor Atualizado |----------")
print(*produtos_atualizados, sep='\n')



produtos_ordenados_por_nome = copy.deepcopy(produtos_atualizados)
produtos_ordenados_por_nome.sort(key = lambda item: item['nome'], reverse = True)

print("\n\n----------| Ordenado por nome |----------")
print(*produtos_ordenados_por_nome, sep='\n')


produtos_ordenados_por_preco = copy.deepcopy(produtos_atualizados)
produtos_ordenados_por_preco.sort(key = lambda item: item['valor'])

print("\n\n----------| Ordenado por preco |----------")
print(*produtos_ordenados_por_preco, sep='\n')