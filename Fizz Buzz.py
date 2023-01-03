a=int(input('Nhap so dau: '))
b=int(input('Nhap so cuoi: '))
if a<b:
    for i in range(a,b+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)
else: print('So dau nho hon so cuoi, vui long lam lai')