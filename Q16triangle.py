a = int(input('1st side : '))
b = int(input('2nd side : '))
c = int(input('3rd side : '))

if a==b==c:
    print('Equilateral Triangle')
elif a==b or b==c or c==a:
    print('isosceles Triangle')
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
    print('Right Angle Triangle')
else:
    print("scalene")
