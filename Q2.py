n = int(input("请输入一个正整数："))
if n ==1:
    print("1不是一个素数")
elif n == 2:
    print("2是一个素数")
else:
     for i in range(2,n):
         if n % i ==0:
             print(f"{n}不是一个素数")
             break
     else:
         print(f"{n}是一个素数")
         
