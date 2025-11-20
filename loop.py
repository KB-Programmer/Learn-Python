# for loop
print("Array Loop Example: \n")
a=["banana","apple","mango"]
for x in a:
     print(f"I like {x}")
     
# while loop

print("\nWhile Loop Example: \n")
i=0
while i<=5:
     print(f"Number {i}")
     i+=1
     
# range for loop

print("\nRange Loop Example: \n")
for x in range(0,12):
     print(f"Range Number {x}")
     
# range div for loop

print("\nRange div for loop Example: \n")
for x in range(0,10,3) :
     print(f"Range Div Number {x}")
     
# conditional loop 
print("\nConditional Loop Example: \n")
for x in range(0,10):
     if x%2==0:
          print(f"{x} is Even")
     else:
          print(f"{x} is Odd")
          
# break for loop
print("\nContinue For Loop Example: \n")
for x in range(0,10):
     if x%2==0:
         continue
     print(x)
     
# Pratical Example
# Pragram that will sum all the numbers from 1 to 20
print("\nPratical Example: Sum of numbers from 1 to 20: \n")
sum=0
for x in range(1,20):
     print(f"{x} to {sum}")
     sum+=x
print(f"\nThe total sum is: {sum}")

#  Program that will print the number from 10 down to 1
print("\nPratical Example: Print numbers from 10 down to 1: \n")
a=10
while a>=0:
     print(a)
     a-=1