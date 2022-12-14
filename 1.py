def sumOfDivBy3and5(num):
    return sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])


print(sumOfDivBy3and5(1000))