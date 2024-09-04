from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_fibonacci_number(num):
    i = 0
    while True:
        fib_num = fibonacci(i)
        if fib_num == num:
            return True
        elif fib_num > num:
            return False
        i += 1

numero = int(input("Informe um número: "))

if is_fibonacci_number(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
