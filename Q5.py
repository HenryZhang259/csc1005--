nums = input("please input a list of integers separated by spaces:")
every_number = nums.split()
largest = int(every_number[0])
for i in every_number:
    x = int(i)
    if x>largest:
        largest=x
print(f"The largest number is:{largest}")
