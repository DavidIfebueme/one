def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def get_digit_sum(n):
    return sum(int(d) for d in str(n))

def get_number_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 else "even")
    return properties
