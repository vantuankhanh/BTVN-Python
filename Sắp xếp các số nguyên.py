def sapxep(num1,num2,num3):
    max1=num1
    a=[num1,num2,num3]
    for i in a:
        if i>max1:
            max1=i
    a.remove(max1)
    if a[0]<a[1]:
        a[0],a[1]=a[1],a[0]
    return [max1,a[0],a[1]]
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print(sapxep(x,y,z))
            