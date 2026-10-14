nums = input("please input a list of integers separated by spaces:")
every_number = nums.split()
max = int(every_number[0])
for i in every_number:
    x = int(i)
    if x>max:
        max=x
print(f"The largest number is:{max}")
