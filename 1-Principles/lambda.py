# Es una fn de una linea:

x = lambda x: x + 5

print(x(2))

# Se suele usar dentro de un map o filter

array = [1,2,3,4,5,6,7,8,9]

mp = map(lambda i: i + 1, array)

print(mp) # ---> devuelve un object dificil de leer

mp2 = list(map(lambda i: i + 1, array))

print(mp2) #--> ahora es una list o array facil de leer

mp3 = list(filter(lambda i: i % 2 == 0, array))

print(mp3)