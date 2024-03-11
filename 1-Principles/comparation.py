# ==
# !=
# <=
# >=
# <
# >

var1 = 1 < 0
var2 = 1 > 0
var3 = 0 != 0

# print(var1, var2, var3)

var4 = var1 or not var2 or var3

print(var4)

var5 = not var1 and not var2

print(var5)