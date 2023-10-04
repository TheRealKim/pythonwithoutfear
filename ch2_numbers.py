# 2.1.1
# Power operator takes precedence over multiplication
print(10*2**2)
print((10*2)**2)

# 2.1.2
# 7 to the 40th power
print(7**40)

# 2.1.3
# Address space of 64-bit architecture
print(64**2)

# 2.1.4
# First number bigger than a google divisible by 13
print((10**100+10) % 13)

# 2.2.1
print('Comma goes 22 places to the right.')

# 2.2.2
# Arithmethic operators have precedence over test-for-equality
print((5+2) == 7)
print(5 + 2 == 2)
print((5*2) == 10)
print(5 * 2 == 2)


# 2.3.1
def quadratic_custom(a, b, c):
    root = (b**2 - 4*a*c)**(0.5)
    determ1 = -b + root
    determ2 = -b - root
    x1 = determ1 / (2 * a)
    x2 = determ2 / (2 * a)
    return x1, x2

print(quadratic_custom(1, -1, -1))

# 2.3.2
try:
    he_loves = 10
    she_loves = -10
    Love = 2
    they_love = he_loves * she_loves + love
except Exception as e:
    print(f"The problem is: {e}")

# 2.3.3
amount = 5
amount55 = 5
_amount = 5
# 1x = 5 Invalid name
y1 = 5
# 2y = 5 Invalid name
n2 = 5

# 2.4.1
a1 = a2 = a3 = 10
print(a1, a2, a3)

# 2.4.2
tt, ty, tz = 10, 20, 30
print(tt, ty, tz)

# 2.4.3
xx = 1.0
print(type(xx))
xx = 1
print(type(xx))
