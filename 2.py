def fibEvenNums(limit):
    a, b = 1, 1
    total = 0
    while a < limit:
        if a % 2 == 0:
            total += a
        a, b = b, a+b
    return total

print(fibEvenNums(4000000))
