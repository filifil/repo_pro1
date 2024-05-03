num = int(input('Enter a number:'))

if num > 1000 and num < 2000:
    print('This number is between 1000 and 2000:',num)
elif num < 1000:
    print('less  number:',num)
elif num > 2000:
    print('more  number:',num)
else:
    print('excluded