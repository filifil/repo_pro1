num = int(input('Enter a number:'))

if num > 1000 and num < 2000:
    print('This number is between 1000 and 2000:')
elif num < 1000:
    print('This number is lower than 1000:')
elif num > 2000:
    print('This number is greater than 2000:')
else:
    print('excluded:')
    