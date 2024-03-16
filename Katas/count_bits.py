# Write a function that takes an integer as input, and returns the number of bits that 
# are equal to one in the binary representation of that number. You can guarantee that 
# input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should 
# return 5 in this case
    

def count_bits(n):
    # bin() transforma en binario con un "0b" delate que indica que es binario
    # Con [2:] estamos haciendo un Slice donde quitamos los dos primeros index -> 0b
    # x = bin(n)[2:]
    
    # Transformamos en un string()
    
    # s = str(x)
    
    # Contamos con el método count()
    
    # response = s.count("1")
    
    return str(bin(n)[2:]).count("1")
    
    
    
count_bits(1234)