def a(x, y):
    return x + y

def b(x, y):
    return x - y

def c(x, y):
    return x * y

def d(x, y):
    return x / y


print("Select an operator")
print("1 +")
print("2 -")
print("3 x")
print("4 :")
p = True
while p == True:
    i = (input("1/2/3/4: "))

    if i in ('1', '2', '3', '4'):
        n1 = eval(input("Enter a number: "))
        n2 = eval(input("Enter another number: "))

        if i == '1':
            print(n1, "+", n2, "=", a(n1, n2))

        elif i == '2':
            print(n1, "-", n2, "=", b(n1, n2))

        elif i == '3':
            print(n1, "x", n2, "=", c(n1, n2))

        elif i == '4':
            print(n1, ":", n2, "=", d(n1, n2))
        
        j = input("Do another calculation ? (y/n): ")
        if j == "n":
          break
          p = False
    
    else:
        print("Enter from 1 - 4")
