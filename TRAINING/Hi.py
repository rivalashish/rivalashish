def Fibonacci():
    print("\n\n####Fibonacci###\n")
    a = 0
    b = 1
    abc = input('Calculate Fibonacci series upto?\t')
    print(a, end=", ")
    print(b, end=", ")
    num1 = int(abc)
    for i in range(0, num1):
        c = a + b
        print(a + b, end=", ")
        a = b
        b = c

# ---------------------------------------------------- #
def Factorial():
    print("\n\n####Factorial###\n")
    t = 1
    fact = 1
    abc = input('Calculate factorial of?\t')
    num = int(abc)
    for j in range(0, num):
        fact = fact * t
        t += 1
    print('Factorial of\t' + str(num) + "\tis\t" + str(fact))

def Coloured():
    from termcolor import colored
    text = colored('\nHello, World!', 'yellow', attrs=['reverse', 'blink'])
    print(text)

# ---------------------------------------------------- #

Factorial()
Fibonacci()
Coloured()
print("hello Mike".find("Mike"));


