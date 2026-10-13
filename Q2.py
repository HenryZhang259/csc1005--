n = int(input("please input an integer N :"))
if n ==1:
    print("1 is not a prime number")
elif n == 2:
    print("2 is a prime number")
else:
     for i in range(2,n):
         if n % i ==0:
             print(f"{n} is not a prime number")
             break
     else:
         print(f"{n} is a prime number")
         
