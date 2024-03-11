#Set es como un array pero no está ordenado por un idex. Existe simplemente el primero y último, lo que lo hace más rápido que los arrays
 
x = set() #----> constructor para un empty set

#Set literal

s = { 1,23,45,2,2,2,2,98,65,25 }

print(type(x), type(s))

# IMPORTANTE -> Si creamos un Set vacío, necesitamos usar un constructor, de otra manera el type será dicctionary

f = {}

print(type(f))

#METHODS 
x.add(2)

s.remove(2)

print(x)
print(s)

x.clear()
print(x)
print(s.difference(x))