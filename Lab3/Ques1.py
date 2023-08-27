import random

def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2
        x = (x * x) % p
    return result

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Find r and d such that n = 2^r * d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n is composite
    return True  # n is probably prime

# Test the algorithm
if __name__ == "__main__":
    num = int(input("Enter a number to test for primality: "))
    iterations = int(input("Enter the number of iterations (default is 5): "))
    
    if miller_rabin(num, iterations):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")

