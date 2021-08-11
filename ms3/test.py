def count_prime_number():
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    if n < m:
        st = n
        en = m
    else:
        st = m
        en = n
    d = 0
    for i in range(st, en + 1):
        s = 0
        for j in range(2, i):
            if i % j == 0:
                s = 1

        if s == 0:
            if i != 1 :
                print(i)
            else :
                d = d - 1
            d += 1
    print('소수 갯수 :', d)


count_prime_number()