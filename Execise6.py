letter= input('Enter your letter betweeen 1 and 5:')

if len(letter)==1:
    print(f'{letter *6}')
elif len(letter)==2:
    print(f'{letter[1]}{letter[0]}')
elif len(letter)==3:
    print(f'{letter[2]}{letter[0]}{letter[1]}')
elif len(letter)==4:
    print(f'{letter[::-1]}')
elif len(letter)==5:
    print(letter[0],letter[1],letter[2],letter[3],letter[4],sep='t')