# isinstance() - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, {0, 1}, True, [0, 1, 2], 
    (1, 2), {'nome': 'Gabriel'},
]

for item in lista:
    if isinstance(item, set):
        print("--- SET ---")
        item.add(2)
        print(f'{item} - é do tipo set: {isinstance(item, set)}')
        print("----------------------------")

    elif isinstance(item, str):
        print("--- STR ---")
        print(f'{item} - é do tipo str: {isinstance(item, str)}')
        print(type(item))
        print("----------------------------")


    elif isinstance(item, (int, float)):
        print("--- Numero ---")
        print(item, item * 3)
        print('É instancia de int: ', isinstance(item, int))
        print('É instancia de float: ', isinstance(item, float))
        print(type(item))
        print("----------------------------")

    else:
        print(f"{item}, que é do tipo {type(item)}")