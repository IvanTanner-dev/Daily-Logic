def convert_parsecs(n):
    multipliers = [3, 2]
    return n * multipliers[n % 2]