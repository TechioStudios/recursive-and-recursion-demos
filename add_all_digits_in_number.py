

def add_digits(n):
    if n // 10 == 0:
        return n
    else:
        return add_digits(n//10) + (n % 10)
while True:
    print(add_digits(int(input("Input number:\n"))))