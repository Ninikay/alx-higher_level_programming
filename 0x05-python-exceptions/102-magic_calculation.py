#!/usr/bin/python3
def magic_calculation(c, k):
    result = 0
    for j in range(1, 3):
        try:
            if j > c:
                raise Exception('Too far')
            else:
                result += (c ** k) / j
        except:
            result = c + k
            break
    return result
