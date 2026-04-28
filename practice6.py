def func(podspisok, spisok):
    it = iter(spisok)  
    for elem in podspisok:    
        if elem not in it:
            return False
    return True


spisok = [
    "купить Amazon",
    "купить Yahoo",
    "купить eBay",
    "купить Yahoo",
    "купить Yahoo",
    "купить Oracle",
]

podspisok = [
    "купить Yahoo",
    "купить eBay",
    "купить Yahoo",
    "купить Oracle",
]

result = func(podspisok, spisok)
print(result)
