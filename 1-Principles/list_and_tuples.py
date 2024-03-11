x = [3, True, "asd"]

print(len(x))

print(x[0])
print(x[1])
print(x[2])

x.append(4)

print(x[3])

x[1] = 19

print(x[1])

x.extend([3,3,3,3,3])

print(x)

print(type(x))

#PARA EVITAR QUE UN CAMBIO AFECTE AL ORIGINAL
print("Se cambia")
#SE CAMBIA
q = [12, 13, 14]
z = q
q[0] = 20

print(q, z)

#NO SE CAMBIA
print("No se cambia")

w = [12, 13, 14]
r = w[:] #PERMANECE INMUTABLE
w[0] = 20

print(w,r)

#TUPLES ->  ES COMO UNA LIST PERO INMUTABLE: NO SE AGREGA, BORRA NI CAMBIA

print("********** TUPLES ***************")

t = (1,2,3,4)
t[0] = 78

print(t)


