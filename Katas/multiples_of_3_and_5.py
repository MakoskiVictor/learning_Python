# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples 
# of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number <= 0:
        return 0
    sum = 0
    for n in range(number):
        if n % 3 == 0  and n % 5 == 0:
            sum += n
        elif n % 3 == 0 or n % 5 == 0: 
            sum += n

    return sum

solution(10)
