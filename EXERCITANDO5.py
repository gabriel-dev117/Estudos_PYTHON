import copy

servidores = [
    {'host': 'srv-01', 'memoria_gb': 8, 'cpu_cores': 4},
    {'host': 'srv-02', 'memoria_gb': 16, 'cpu_cores': 8},
    {'host': 'srv-03', 'memoria_gb': 4, 'cpu_cores': 2}
]

servidores_upgraded = [
    {**h, 'memoria_gb':  h['memoria_gb'] * 2, 'datacenter': 'SP-1'}
    for h in copy.deepcopy(servidores)
]
print("-----| Lista Original |-----")
print(*servidores, sep='\n')
print()
print("-----| Lista Atualizada |-----")
print(*servidores_upgraded, sep='\n')