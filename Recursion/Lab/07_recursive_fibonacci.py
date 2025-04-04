def fib(n):
    fib0 = 1
    fib1 = 1

    result = 0

    for _ in range(n - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result

    return result


n = int(input())

print(fib(n))