def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

val_1 = is_prime(3)
print(val_1)
val_2 = is_prime(14)
print(val_2)