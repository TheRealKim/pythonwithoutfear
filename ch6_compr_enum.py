# table.py

def table():
    fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    format_str = '{:>2}. {:>4}'
    for i, item in enumerate(fib_list, 1):
        print(format_str.format(i, item))

# table()

# 6.1.1
def table2():
    fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    format_str = '{:>2}. {:>4}'
    for i in range(len(fib_list)):
        print(format_str.format(i+1, fib_list[i]))

# table2()

# 6.1.2
def fibonacci():
    fib = [1, 1]
    while len(fib) < 11:
        fib.append(fib[len(fib)-2]+fib[len(fib)-1])
    return fib

def table3():
    fib_list = fibonacci()
    format_str = '{:>2}. {:>4}'
    for i in range(len(fib_list)):
        print(format_str.format(i + 1, fib_list[i]))

# table3()

# 6.1.3
def table4():
    fib_list = fibonacci()
    format_str = '{:>3}. {:>5}. {:>5}'
    for i, item in enumerate(fib_list, 0):
        if i >= 1:
            print(format_str.format(i-1, item, fib_list[i]-fib_list[i-1]))
        else:
            print(format_str.format(i-1, item, 0))

# table4()

# squares.py
def squares():
    sqr_list = [i * i for i in range(1, 7)]
    format_str = '{:>3}  {:>3}  {:>3}'
    old_val = 0
    for i, item in enumerate(sqr_list, 1):
        print(format_str.format(i, item, item - old_val))
        old_val = item

# squares()

# 6.2.1
def squares2():
    n = int(input('Calculate how many products? '))
    sqr_list = [i * i for i in range(1, n+1)]
    format_str = '{:>4}  {:>4}  {:>4}'
    old_val = 0
    for i, item in enumerate(sqr_list, 1):
        print(format_str.format(i, item, item - old_val))
        old_val = item

# squares2()

# 6.2.2
def squares3():
    n = int(input('Calculate how many products? '))
    sqr_list = [i * i for i in range(1, n + 1)]
    format_str = '{:>4}  {:>4}  {:>4}  {:>4}'
    old_val = 0
    for i, item in enumerate(sqr_list, 1):
        print(format_str.format(i, item, item - old_val, (item * item * item)))
        old_val = item

# squares3()


# 6.2.3
def squares4():
    n = int(input('Calculate how many products? '))
    sqr_list = [i * i for i in range(1, n + 1)]
    format_str = '{:>4}  {:>4}  {:>4}  {:>4}'
    for i in range(len(sqr_list)):
        if i == 0:
            print(format_str.format(i+1, sqr_list[i], 1, 1))
        else:
            print(format_str.format(i+1, sqr_list[i], sqr_list[i] - sqr_list[i-1], sqr_list[i]**3))

# squares4()


# sieve2
def sieve2():
    n = int(input('Enter value of n as max prime number (0 to quit): '))
    while n != 0:
        comp_list = [j for i in range(2, n) for j in range(i*i, n, i)]
        print(comp_list)
        prime_list = [i for i in range(2, n) if i not in comp_list]
        print(prime_list)
        n = int(input('\nEnter value of n (0 to quit): '))
    print('Bye')

# sieve2()

def sets():
    n = int(input('Enter value of n as max prime number (0 to quit): '))
    while n != 0:
        comp_set = {j for i in range(2, n) for j in range(i * i, n, i)}
        print(comp_set)
        prime_list = [i for i in range(2, n) if i not in comp_set]
        print(prime_list)
        n = int(input('\nEnter value of n (0 to quit): '))
    print('Bye')

# sets()

# 6.3.1
def sieve3():
    n = int(input('Enter value of n as how many prime numbers you want(0 to quit): '))
    while n != 0:
        prime_list = [2, 3]
        i = 4
        while len(prime_list) < n:
            for j in prime_list:
                if i % j == 0:
                    i += 1
                    break
            else:
                prime_list.append(i)
                i +=1
        print(prime_list)
        print(len(prime_list))

# sieve3()

# 6.3.2
def sieve4():
    n = int(input('Enter value of n as max prime number (0 to quit): '))
    while n != 0:
        comp_list = [j for i in range(2, n) for j in range(i * i, n, i)]
        print(comp_list)
        prime_list = [i for i in range(2, n) if i not in comp_list]
        for i in prime_list:
            print(i, end=" ")
        n = int(input('\nEnter value of n (0 to quit): '))
    print('Bye')

# sieve4()

# 6.3.3
def triangle():
    n = int(input('Enter value of n as max number to calculate triangle for: '))
    triangle_list = [int(i*(i+1)/2) for i in range(1, n)]
    print(triangle_list)

# triangle()

# 6.3.4
def triangle2():
    n = int(input('Enter value of n as max number to calculate triangle for: '))
    triangle_list = [int(i*(i+1)/2) for i in range(1, n)]
    even_triangle_list = [item for item in triangle_list if item % 2 == 0]
    print(even_triangle_list)

# triangle2()

# 6.3.5
def evens_odds():
    n = int(input('Enter value of n as max number to calculate evens/odds for : '))
    evens = [i for i in range(1, n+1) if i % 2 == 0]
    odds = [i for i in range(1, n+1) if i not in evens]
    print(f'evens: {evens}')
    print(f'odds: {odds}')

# evens_odds()

# pythag.py
def pythag():
    n = int(input('Enter value of n as max number to calculate pythagoras triples for : '))
    nums = range(1, n+1)
    trips = [(a, b, c) for a in nums for b in nums for c in nums if (a**2+b**2 == c**2)]
    print(trips)

# pythag()

# 6.4.1
def pythag():
    n = int(input('Enter value of n as max number to calculate pythagoras triples for : '))
    nums = range(1, n+1)
    trips = [(a, b, c) for a in nums for b in nums for c in nums if (a**2+b**2 == c**2)]
    for i in trips:
        format_str = '{:>3} {:>3} {:>3}'
        a, b, c = i
        print(format_str.format(a, b, c))

# pythag()

# 6.4.2
def quadsum_less_than_100():
    quadsum = [(a, b) for a in range(1, 11) for b in range(1, 11) if a**2 + b**2 < 100]
    for i in quadsum:
        a, b = i
        format_str = '{:>3} {:>3} {:>3}'
        print(format_str.format(a**2, b**2, a**2 + b**2))

# quadsum_less_than_100()

#6.4.3
def pythag_quad():
    pyth_quad = [
        (a, b, c, d)
        for a in range(1, 11)
        for b in range(1, 11)
        for c in range(1, 11)
        for d in range(1, 11)
        if a**2 + b**2 + c**2 == d**2
    ]
    for item in pyth_quad:
        print(item)

pythag_quad()

#6.4.4
def pythag_var_power():
    # Doesn't exist for p > 3
    n = int(input('Enter value of n as max number to calculate pythagoras triples for : '))
    p = int(input('Enter value for the power: '))
    nums = range(1, n + 1)
    pythag_list = [
        (a, b, c)
        for a in nums
        for b in nums
        for c in nums
        if a**p + b**p == c**p
    ]
    print(pythag_list)

pythag_var_power()