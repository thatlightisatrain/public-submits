def rangecheck(i, start, end):
    if i in range(start, end + 1):
        print(f"{i} is in the range from {start} to {end}")
    else:
        print(f"{i} is outside given range")
        
rangecheck(5, 2, 7)