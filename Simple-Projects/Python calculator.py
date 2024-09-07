print("Enter first number: ")
a=int(input())
print("Enter second number: ")
b=int(input())
print("Enter operator: ")
op=input()

if op=="+":
    c=a+b
elif op=="-":
    c=a-b
elif op=="*":
    c=a*b
elif op=="/":
    c=a/b
elif op=="**":
    c=a**b
elif op=="//":
    c=a//b
elif op=="%":
    c=a%b
else: c=None

if c==None:
    print("Operator not valid!")
else: print(a, op, b, "=", c)    