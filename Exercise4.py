a = int(input('Enter the 1st number:'))
b = int(input('Enter the 2nd number:'))
c = int(input('Enter the 3rd number:'))
d = int(input('Enter the 4th number:'))

if a > b and a > c and a > d:
    print('The largest number is',a)
elif b > a and b > c and b > d:
    print('The largest number is',b)
elif c > a and c > b and c >d:
    print('The lagest number is',c)
else:
    print('The largest number is',d)
    
