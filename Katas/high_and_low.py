# n this little assignment you are given a string of space separated numbers, and have to 
# return the highest and lowest number.
# Examples

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes

#     All numbers are valid Int32, no need to validate them.
#     There will always be at least one number in the input string.
#     Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low (numbers):
    if not isinstance(numbers, str):
        raise ValueError("The ags should be a string")

    numeros_str = numbers.split()
    
    number = [int(num) for num in numeros_str]
    
    high_number = max(number)
    low_number = min(number)
    
    return f"{high_number} {low_number}"
