def my_factorial(n):
    factorial = 1

    if n < 0:
        print("Sorry, factorial does not exist for negative numbers!")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
    return factorial

input1 = int(input("Enter a number: "))
fact = my_factorial(input1)
print("The factorial of ", input1, " is ", fact)