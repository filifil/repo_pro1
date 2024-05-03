off_days1 = [8,12,8,20]
sum_off = sum(off_days1)
off_days2 = [16,7,5,22]
buzy = 365-int(sum_off)

if off_days1:
    print('Frank was sick for',sum_off,'days')
    print('He went dancing',buzy,'days')

else:
    print("he can't be sick for negative days")

