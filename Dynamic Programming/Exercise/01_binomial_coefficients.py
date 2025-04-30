n = int(input())
k = int(input())


def binomial_coefficients(n, k, memo):
    key = f"{n} {k}"

    if key in memo:
        return memo[key]

    if n == 0 or k == 0 or n==k:
        return 1

    result = binomial_coefficients(n - 1, k - 1, memo) + binomial_coefficients(n - 1, k, memo)
    memo[key] = result

    return result


print(binomial_coefficients(n, k, {}))