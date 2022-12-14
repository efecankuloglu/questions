def palindrome_num():
    pal_num_list = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            multiplied = i * j
            if str(multiplied) == str(multiplied)[::-1]:
                pal_num_list.append(multiplied)
    return max(pal_num_list)


print(palindrome_num())