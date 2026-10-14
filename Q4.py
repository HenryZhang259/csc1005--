n = input("please input a non-negative integer n:")
try:
    n = int(n)
    if n < 0 :
        raise ValueError
except ValueError:
    print(" value error！please input a non-negative integer n！！！")
else:
    if n == 0:
        print("The factorial of 0 is : 1")
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial = factorial*i
        print(f"The factorial of {n} is:{factorial}")