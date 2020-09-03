n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 0
num2 = 0
num3 = 1

for i in range(n):
    sum_int = num1 + num2 + num3
    num1 = num2
    num2 = num3
    num3 = sum_int
    print(sum_int)
    
