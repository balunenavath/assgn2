#Code 1:


num1 = int(input("Enter first number: "))
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

num2 = int(input("Enter second number: "))
if num2 % 2 == 0:
    print(f"{num2} is an even number.")
else:
    print(f"{num2} is an odd number.")

#Code 2:

num = 0
for i in range(0,51):
    num+=i
print('The sum of the numbers from 1 to 50 is: ',num)