def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(number):
    return "Prime" if is_prime(number) else "Not Prime"


#Test1

print(check_prime(7))


#Test 2

print(check_prime(4))
