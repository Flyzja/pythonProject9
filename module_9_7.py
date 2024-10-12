def is_prime(func):
    def wrapper(*numbers):
        number = func(*numbers)
        for i in range(2, number):
            if number % i == 0:
                return "Составное"
            else:
                return "Простое"
        return number
    return wrapper

@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 4, 7)
print(result)

