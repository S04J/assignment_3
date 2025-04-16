def factorial(n):
    if n>=0 and n<2:
        return 1
    else:
        return n*factorial(n-1)
res=factorial(5)
print(res)