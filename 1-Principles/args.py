# * desempaqueta arrays o lists (quita los corchetes) y ** desempaqueta dictionaries (quita las llaves)

def funcione(x, y):
    print(x,y)
    
pairs = [(1,2),(3,4)]

for pair in pairs:
    funcione(*pair)

dictionaries = {"x": 25, "y": 35}

funcione(**dictionaries)

# Básicamente, hace un mapeo

def newfn(*args, **kwargs):
    print(args, kwargs)
    
newfn(1,2,3,4,"asdasd", "sad", one=0, str="qweqw")