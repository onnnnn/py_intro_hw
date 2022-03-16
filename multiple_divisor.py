def is_multiple(c, a):
    '''判斷 c 是不是 a 的倍數'''

    # 如果 c 可以被 a 整除
    if c % a == 0:
        return f'Yes, {c} 是 {a} 的倍數'
    else:
        return f'No, {c} 不是 {a} 的倍數'


def is_divisor(a, b):
    '''判斷 a 是不是 b 的因數'''

    # 所有可以整除 b 的值都放進來
    possible_divisor = []

    for i in range(1, b+1):
        if b % i == 0:
            possible_divisor.append(i)

    # 看 a 有沒有在 `possible_divisor` 裡面
    if a in possible_divisor:
        return f'Yes, {a} 是 {b} 的因數'
    else:
        return f'No, {a} 不是 {b} 的因數'


print(is_multiple(16, 2))  # Yes
print(is_multiple(11, 3))  # No

print(is_divisor(2, 8))  # Yes
print(is_divisor(8, 2))  # No
