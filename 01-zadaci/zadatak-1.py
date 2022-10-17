def func1(lista):
    assert isinstance(lista, list)
    assert all(isinstance(x, str) for x in lista)
    return {k:v[::-1] for k,v in enumerate(lista)}

print(func1(['Stol', 'Stolica', 'Krevet', 'Fotelja']))