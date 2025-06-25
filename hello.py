def greet():
    x=input("e:")
    print("hello")

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
try:
    ans=a/b
    print(ans)
    greet()
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

