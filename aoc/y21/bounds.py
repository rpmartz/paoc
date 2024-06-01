def calc(firstDigit, secondDigit, thirdDigit):
    z = (((((firstDigit + 13) * 26) + (secondDigit + 10)) * 26) + (thirdDigit + 3))

    return z


if __name__ == '__main__':
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                z = (((((a + 13) * 26) + (b + 10)) * 26) + (c + 3))
                z_mod_26 = z % 26
                if z_mod_26 >= 12 and z_mod_26 <= 20:
                    print(f'{a}, {b}, {c} produce {z} which mod 26 is {z_mod_26}')
