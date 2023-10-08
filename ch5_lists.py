# sort.py
def sort_list():
    a_list = []
    while True:
        str1 = input('Enter a name; ')
        if not str1:
            break
        a_list.append(str1)
    a_list.sort()
    print('Here is the alpha sorted list ...')
    for str1 in a_list:
        print(str1)

# sort_list()

# 5.1.1
def sort_list_2():
    a_list = []
    while True:
        str1 = input('Enter a name; ')
        if not str1:
            break
        a_list.append(str1)
    print(f'The amount of names is: {len(a_list)}')
    a_list.sort()
    print('Here is the alpha sorted list ...')
    for str1 in a_list:
        print(str1)

# sort_list_2()

# 5.1.2
def sort_list_3():
    a_list = []
    while True:
        str1 = input('Enter a name; ')
        if not str1:
            break
        a_list.append(str1)
    print(f'The amount of names is: {len(a_list)}')
    a_list.sort()
    print('Here is the alpha sorted list ...')
    for str1 in a_list:
        print(str1, end=" ")

# sort_list_3()

# 5.1.3
def sort_list_4():
    a_list = []
    while True:
        fl1 = float(input('Enter a number (0 to exit); '))
        if fl1 == 0:
            break
        a_list.append(fl1)
    print(f'The amount of numbers is: {len(a_list)}')
    a_list.sort()
    print('Here is the sorted list ...')
    for fl1 in a_list:
        print(fl1, end=" ")

# sort_list_4()


# fact2.py
def fact2():
    n = int(input('Calculate factorial for which n? '))
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    print('The result is: ', prod)

# fact2()

# 5.2.1
def fact3():
    n = int(input('Calculate factorial for which n? '))
    while n != 0:
        prod = 1
        for i in range(1, n+1):
            prod = prod * i
        print('The result is: ', prod)
        n = int(input('Calculate factorial for which n? '))

# fact3()

# prime.py
def prime():
    bool_list = [True] * 100
    for prime in range(2,100):
        if bool_list[prime]:
            print(prime, end=' ')
            for i in range(prime * 2, 100, prime):
                bool_list[i] = False

# prime()

def prime2():
    bool_list = [True] * 100
    primes_found_list = []
    for prime in range(2,100):
        if bool_list[prime]:
            primes_found_list.append(str(prime))
            for i in range(prime * 2, 100, prime):
                bool_list[i] = False
    out_str = ' '.join(primes_found_list)
    print(out_str)

# prime2()



# 5.3.1
def prime3():
    n = int(input('Calculate the primes up until? '))
    bool_list = [True] * n
    primes_found_list = []
    for prime in range(2,n):
        if bool_list[prime]:
            primes_found_list.append(str(prime))
            for i in range(prime * 2, n, prime):
                bool_list[i] = False
    out_str = ' '.join(primes_found_list)
    print(out_str)

# prime3()

# 5.3.2
def prime4():
    n = int(input('Calculate the primes up until? '))
    bool_list = [True] * n
    primes_found_list = []
    for prime in range(2,n):
        if bool_list[prime]:
            primes_found_list.append(str(prime))
            for i in range(prime * 2, n, prime):
                bool_list[i] = False
    out_str = ' '.join(primes_found_list)
    n_primes = len(primes_found_list)
    print(out_str)
    print(f'number of primes:', n_primes)

# prime4()

def prime5():
    n = int(input('Calculate the primes up until? '))
    bool_list = [True] * n
    primes_found_list = []
    n_primes = 0
    for prime in range(2,n):
        if bool_list[prime]:
            primes_found_list.append(str(prime))
            n_primes += 1
            for i in range(prime * 2, n, prime):
                bool_list[i] = False
    out_str = ' '.join(primes_found_list)
    print(out_str)
    print(f'number of primes:', n_primes)

# prime5()

# 5.3.3
def prime6():
    # n = int(input('Calculate the primes up until? '))
    n = 100
    bool_list = [True] * n
    primes_found_list = []
    n_primes = 0
    for prime in range(2, n):
        if bool_list[prime]:
            primes_found_list.append(str(prime))
            n_primes += 1
            prime_base = prime * 2
            while prime_base < n:
                bool_list[prime_base] = False
                prime_base += prime
    out_str = ' '.join(primes_found_list)
    print(out_str)
    print(f'number of primes:', n_primes)

# prime6()



