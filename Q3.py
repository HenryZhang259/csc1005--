n = input("please input an integer bigger than one:")
try:
    n = int(n)
    if n < 0 :
        print(" value error！please input an integer bigger than one！！！")
except ValueError:
    print(" value error！please input an integer bigger than one！！！")
else:
    for num in range(1,n+1):
        if num ==1:
            print(1,end="\n")
        else:
            for i in range(1,num+1):
                print(i,end = " ")
            print()
    