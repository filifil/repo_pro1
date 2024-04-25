bto=int(input('Enter salary:'))
sala1 = 67000*0.24
sala2 = 97000*0.31
sala3 =97000*0.34

if (bto)<67000 and bto*0.24:
    print(sala1,'have to pay:')
elif int(bto)<97000 and bto*0.31:
    print(sala2,'have to pay:')
elif int(bto) > 97000 and bto*0.34:
    print(sala3,'have to pay:')