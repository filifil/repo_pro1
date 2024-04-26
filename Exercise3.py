a = float(input('Enter the first number'))
b = float(input('Enter the second number'))
c = float(input('Enter the third number'))
d=a+b+c
e=a*b*c
f=d*4

if a==b==c:
    print('product:',f)
elif a!=b!=c:
    print('sum:',d)
else:
    print('unknown:')

