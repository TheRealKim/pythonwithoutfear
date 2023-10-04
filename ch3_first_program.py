# 3.1.1
def quadratic_custom(a, b, c):
    root = (b**2 - 4*a*c)**(0.5)
    determ1 = -b + root
    determ2 = -b - root
    x1 = determ1 / (2 * a)
    x2 = determ2 / (2 * a)
    return x1, x2

# 3.1.2
x1, x2 = quadratic_custom(1, -1, -1)
print('The x1 value is', x1, 'and the x2 value is', x2)
# Putting a '.' after the sentence
print('The x1 value is', x1, 'and the x2 value is', x2, '.') #prints space before dot
print('The x1 value is ', x1, ' and the x2 value is ', x2, '.', sep='')
print('The x1 value is {} and the x2 value is {}.'.format(x1, x2))
print(f'The x1 value is {x1} and the x2 value is {x2}.')

# 3.1.3
phi, x = quadratic_custom(1, -1, -1)
print(1/phi)

# 3.2.1
a = float(input("Enter the value of the x-square coefficient: "))
b = float(input("Enter the value of the x coefficient: "))
c = float(input("Enter the value of the constant: "))
print(quadratic_custom(a, b, c))

# 3.2.2
while True:
    try:
        a = int(input("Enter the value of the x-square coefficient: "))
        b = int(input("Enter the value of the x coefficient: "))
        c = int(input("Enter the value of the constant: "))
        break
    except:
        print("Only integers are accepted as an input")
print(quadratic_custom(a, b, c))

# 3.2.3
def calculate_triangle_area(w, h):
    return w * h * 0.5

w = float(input("The width of the triangle is: "))
h = float(input("The height of the triangle is: "))
area = calculate_triangle_area(w, h)
print("The area of the triangle is", area)

# 3.2.4
# V = 4/3 π r³
import math
r = float(input("The radius of the sphere: "))
volume = (4/3) * math.pi * r**3
print("Volume of the sphere is", volume)

# 3.3.1
def dist(x1, y1, x2, y2):
    h_dist = x2 - x1
    v_dist = y2 - y1
    dist = (h_dist ** 2 + v_dist ** 2) ** 0.5
    return dist

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
dist = dist(x1, y1, x2, y2)
print('The distance is', dist)

# 3.3.2
print('The distance is {}.'.format(dist))

# 3.3.3
area = calculate_triangle_area(w, h)
print('The area of a triangle is {}'.format(area))

# 3.3.4
def circle_area(r):
    area = math.pi * r**2
    return area

r2 = float(input('Enter radius of the circle: '))
area = circle_area(r2)
print('The area of a triangle is {}'.format(area))
