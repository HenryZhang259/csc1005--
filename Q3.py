n = input("please input an integal bigger than one:")
try:
    n = int(n)
    if n <= 1 :
        print(" value error！please input an integal bigger than one！！！")
except ValueError:
    print(" value error！please input an integal bigger than one！！！")
for num in range(1,n+1):
    if num ==1:
        print(1,end="\n")
    else:
        for i in range(1,num+1):
            print(i,end = "\n")


    