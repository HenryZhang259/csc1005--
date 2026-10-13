n = input("please input an integer N bigger than 0:")
try:
    n = int(n)
    if n <= 0 :
        raise ValueError
except ValueError:
    print(" value error！please input an integer bigger than 0！！！")
else:
    for i in range(1,n):
        for f in range(1,i):
            sum = 0
            if n % f == 0:
                sum += f
        if sum == n:
            print(n , end="\n")