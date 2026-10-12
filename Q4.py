n = input("please input an integer N bigger than 0:")
try:
    n = int(n)
    if n <= 0 :
        raise ValueError
except ValueError:
    print(" value error！please input an integer bigger than 0！！！")
else:
    if n == 1:
        print("The factorial of 1 is : 1")
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial = factorial*i
        print(f"The factorial of {n} is:{factorial}")