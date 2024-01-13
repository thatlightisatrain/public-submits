def highest(numbers):
    maxnum= 0
    for number in numbers:
        if number >= maxnum:
            maxnum = number
    else:
        return maxnum
    
numbers = [4,999,6,7,54]
print(highest(numbers))