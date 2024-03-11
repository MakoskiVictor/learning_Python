x = [0,1,2,3,4,5,6,7,8,9,10]

# x[start : stop : step(increse)]  ==> stop no toma el último valor => termina ni bien llegar al valor
sliced = x[0:4:2]

sliced2 = x[0:5:1]

sliced3 = x[0:len(x)]

sliced4 = x[:7]

# Usar step negativo hace que vayamos en reversa

sliced5 = x[9::-1]

print(sliced)
print(sliced2)
print(sliced3)
print(sliced4)
print(sliced5)