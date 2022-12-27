a=float(input('Nhap chieu cao: '))
b=float(input('Nhap can nang: '))
bmi=b/(a**2)
if bmi<16:
    print('Gầy cấp độ III')
elif 16<=bmi<17:
    print('Gầy cấp độ II')
elif 17<=bmi<18.5:
    print('Gầy cấp độ I')
elif 18.5<=bmi<25:
    print('Bình thường')
elif 25<=bmi<30:
    print('Thừa cân')
elif 30<=bmi<35:
    print('Béo phì cấp độ I')
elif 35<=bmi<40:
    print('Béo phì cấp độ II')
else:
    print('Béo phì cấp độ III')