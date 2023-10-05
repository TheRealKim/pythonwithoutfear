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

sort_list_4()
