# Are like objects in JavaScript
# Use Key - Value

x = {"key": 4}

print(x["key"])

x["key2"] = "This is the key 2"

print(x["key2"])

x[1] = [2,3,4,5,12,13,14,15]

print(x[1])

print(x.keys())

print(x.values())

print(x.items())

# LOOPS

for key, values in x.items():
    print(key, values)




# ELIMINAR KEY - VALUE

del x["key2"]

print(x)