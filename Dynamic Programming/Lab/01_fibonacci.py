def fib(n, memo):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result

n = int(input())
print(fib(n,{}))