def éPrimo (x):

    divisor = 2

    if x == 2:

        return True

    while x % divisor != 0 and divisor <= x / 2:

        divisor = divisor + 1

    if x % divisor == 0:

        return False

    else:

        return True

n = int(input("Digite um número inteiro: "))

while n > 0:

    if éPrimo(n):

        print(n, "é primo!")

    else:

        print(n, "não é primo...")

    n = int(input("Digite um número inteiro: "))
