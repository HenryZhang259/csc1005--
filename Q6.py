n = input("please input an integer N bigger than 0:")
try:
    n = int(n)
    if n <= 0 :
        raise ValueError
except ValueError:
    print(" value error！please input an integer bigger than 0！！！")
else:
    for i in range(1,n):
        sum = 0
        for f in range(1,i):
            if i % f == 0:
                sum = f + sum
        if sum == i:
            print(i , end="\n")
