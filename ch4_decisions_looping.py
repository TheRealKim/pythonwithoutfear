# age.py
def main():
    age = int(input('Enter your age, please: '))
    name_str = input('Enter your name, please: ')
    print('Happy birthday, ', name_str, '.', sep='')
    print('You are', age, 'years old.')
    if age > 12 and age < 20:
        print('You are a teenager!')
    else:
        print('You\'re NOT a teenager!')

# main()

# 4.1.1
def test_between_one_and_hundred():
    lower = 1
    upper = 100
    number = int(input('Enter a number, please: '))
    if number >= lower and number <= upper:
        print(f'Number is within range of {lower} and {upper}.')
    else:
        print(f'Number is out of range of {lower} and {upper}.')

# test_between_one_and_hundred()

# 4.1.2
def test_between_one_and_hundred_2():
    lower = 1
    upper = 100
    number = int(input('Enter a number, please: '))
    if not (number <= lower or number >= upper):
        print(f'Number is within range of {lower} and {upper}.')
    else:
        print(f'Number is out of range of {lower} and {upper}.')

# test_between_one_and_hundred_2()

# 4.1.3
def test_multiple():
    multiple = 7
    number = int(input('Enter a number, please: '))
    remainder = number % 7
    if remainder == 0:
        print(f'Number is a multiple of {multiple}.')
    else:
        print(f'Numbber is not a multiple of {multiple} and the remainder is {remainder}.')

# test_multiple()

# fact.py and 4.2.1
def fact():
    n = int(input('Enter value of n (0 to quit): '))
    while n != 0:
        prod = i = 1
        while i <= n:
            prod *= i
            i += 1
        print(f'The factorial of {n} is {prod}.')
        n = int(input('Enter value of n (0 to quit): '))
    print('Bye Now!')

# fact()

# 4.2.2
def triangle_num():
    n = int(input('Enter value of n (0 to quit): '))
    while n != 0:
        sum_int = 0
        i = 1
        while i <= n:
            sum_int += i
            i += 1
        print(f'The triangle number of {n} is {sum_int}.')
        n = int(input('Enter value of n (0 to quit): '))
    print('Bye Now!')

# triangle_num()

# 4.2.3
def triangle_num_and_test():
    n = int(input('Enter value of n (0 to quit): '))
    while n != 0:
        sum_int = 0
        i = 1
        while i <= n:
            sum_int += i
            i += 1
        print(f'The triangle number of {n} is {sum_int}.')
        if sum_int == n*(n+1)/2:
            print(f'The theorem holds up.')
        n = int(input('Enter value of n (0 to quit): '))
    print('Bye Now!')

# triangle_num_and_test()


# fibonacci.py and 4.3.1
def fibonacci():
    n = int(input('Enter value of n (0 to quit): '))
    while n!=0:
        a = b = 1
        print(a, end=" ")
        print(b, end=" ")
        while (a + b) < n:
            a, b = a + b, a
            print(a, end=" ")
        n = int(input('\nEnter value of n (0 to quit): '))
    print('Bye')

# fibonacci()

# 4.3.2
def get_golden_ratio():
    n = int(input('Enter value of n (0 to quit): '))
    while n != 0:
        a = b = 1
        while (a + b) < n:
            a, b = a + b, a
        print(a/b, end=" ")
        n = int(input('\nEnter value of n (0 to quit): '))
    print('Bye')

# get_golden_ratio()

# guessing.py and 4.3.1
import random
def guess():
    # n = random.randint(1, 50)
    n = random.randint(1, 100)
    while True:
        ans = int(input('Enter your guess: '))
        if ans == n:
            print('Success! You win!')
            break
        elif ans > n:
            print('Too high.')
        else:
            print('Too low.')

# guess()

# 4.3.2
def guess_2():
    lower = 1
    upper = 100
    n = random.randint(lower, upper)
    print(f"You will need to guess a number between {lower} and {upper}.")
    while True:
        ans = int(input('Enter your guess: '))
        if ans == n:
            print('Success! You win!')
            break
        elif ans > n:
            print('Too high.')
        else:
            print('Too low.')

# guess_2()

# 4.3.3
def guess_3():
    lower = 1
    upper = 10
    n = random.randint(lower, upper)
    ans = 1
    while ans != 0:
        print('Let\'s play a new game')
        print(f"You will need to guess a number between {lower} and {upper}.")
        while True:
            ans = int(input('Enter your guess (Enter 0 to stop playing): '))
            if ans == 0:
                print('Ending the game.')
                break
            elif ans == n:
                print('Success! You win!')
                break
            elif ans > n:
                print('Too high.')
            else:
                print('Too low.')

# guess_3()

# 4.3.4
def guess_4():
    lower = int(input('Enter your lower limit: '))
    upper = int(input('Enter your upper limit: '))
    n = random.randint(lower, upper)
    ans = 1
    while ans != 0:
        print('Let\'s play a new game')
        print(f"You will need to guess a number between {lower} and {upper}.")
        while True:
            ans = int(input('Enter your guess (Enter 0 to stop playing): '))
            if ans == 0:
                print('Ending the game.')
                break
            elif ans == n:
                print('Success! You win!')
                break
            elif ans > n:
                print('Too high.')
            else:
                print('Too low.')

guess_4()


