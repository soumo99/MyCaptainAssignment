n_terms = int(input("Enter the number of terms need to be displayed :"))

num1 = 0
num2 = 1
next=0

if n_terms <= 0:
    print("pls enter a valid positive integer")
elif n_terms == 1:
    print("Fibonacci series upto :", n_terms)
    print(num1)
else:
    print("Fibonacci series : ")
    
    while next < n_terms:
        print(num1 , end=" ")

        sum = num1 + num2

        num1 = num2
        num2 = sum
        next += 1

