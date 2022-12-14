def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nth_prime_num(num):
    n = 2
    while num > 0:
        if is_prime(n):
            num -= 1
        n += 1
    n -= 1
    return n

print(nth_prime_num(10001))