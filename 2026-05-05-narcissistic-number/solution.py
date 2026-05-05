def is_narcissistic(n):
    s = str(n)
    p = len(s)
    return sum(int(d) ** p for d in s) == n