def function(d1, d2):
    assert isinstance(d1, dict) and isinstance(d2, dict)
    assert all(isinstance(l, list) for _,i in d1.items()) and all(isinstance(l, list) for _,i in d2.items()) 
    assert all(list(x.keys()) == ["valute", "cijena"])
    return []

print(function({"valute": ["GBP", "USD", "CZK", "Error"], "cijena": [8,5,7,7,0.3,10,3]}, {"valute": ["EUR","USD", "CZK", "Error"], "cijena": [7,5,7,7,0.3,5,5]}))