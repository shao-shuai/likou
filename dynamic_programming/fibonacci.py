def fib(n, nb = {}):
    if n == 0 or n == 1:
        return n
    
    if n in nb:
        return nb[n]

    val = fib(n - 1) + fib(n - 2)

    nb[n] = val

    return val

print(fib(15))