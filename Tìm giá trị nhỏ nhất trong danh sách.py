def find_min(a):
    min1=a[0]
    for i in a:
        if i<min1:
            min1=i
    return min1
num=[1129,254,123,6231,6,123,6,123231,6574,235,4581]
print(find_min(num))
            