#try catch
x = "asd"
y= 12
try:
    x + y
except Exception as e:
    print(e)
finally:
    print("Llegamos hasta acá victoriosos")

# Maneras de thrown an error

raise Exception("Bad method")

