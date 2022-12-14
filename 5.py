def noNoneValueList(lt):
    new_lt = []
    for i in range(0, len(lt)):
        if lt[i] is None:
            for j in range(i - 1, -1, -1):
                if lt[j] is not None:
                    new_lt.append(lt[j])
                    break
        else:
            new_lt.append(lt[i])
    return new_lt


print(noNoneValueList([3, None, 2, None, None, 1, False, None, 10]))
