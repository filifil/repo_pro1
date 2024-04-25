q1=int(input('what is 3* 4?:'))
contenuequstion=True
if q1 != 12:
    contenuequstion=False
else:
    print("That is correct!")
    q2=int(input('what is 6* 5?:'))
    if q2 != 30:
        contenuequstion=False
    else:
        print("That is also correct!")
        q3=int(input('what is 7* 8?:'))
        if q3 != 56:
            contenuequstion=False
        else:
            print('correct!you pass the test')
if not contenuequstion:
    print('That is False,you failed the test')