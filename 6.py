import string

def avg_len(str):
    alphabet_lt = list(string.ascii_lowercase)

    str_lt = str.split()
    str_count = len(str_lt)
    str_char_count = len([i for i in str.lower() if i in alphabet_lt])

    return str_char_count / str_count



print(avg_len("Elma, portakal, armut"))
