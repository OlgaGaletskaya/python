def zeros(n):
    result = 0
    col = 5
    while col <= n:
        result += n//col
        col *= 5
    return result

