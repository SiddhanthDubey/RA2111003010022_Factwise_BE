sd = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
dd1 = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 9, 19: 8}
dd2 = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
td = {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}
cd = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
      17: 9, 18: 9, 19: 8}


def count_word(n):
    if n < 10:
        return sd[n % 10]
    elif n < 100:
        if n < 20:
            return dd1[n]
        else:
            return dd2[int(n / 10)] + sd[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return sd[int(n / 100)] + 7
        elif n % 100 < 20:
            return td[int(n / 100)] + cd[n % 100]
        else:
            return td[int(n / 100)] + dd2[int((n % 100) / 10)] + sd[n % 10]


count = 0
for i in range(1000):
    # print(i, count, count_word(i))

    count = count + count_word(i)

print(count)

# Output For Above Code Is : 21123
