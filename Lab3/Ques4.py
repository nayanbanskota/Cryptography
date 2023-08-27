def power(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2
        x = (x * x) % p
    return result

def diffie_hellman(p, g, private_a, private_b):
    public_a = power(g, private_a, p)
    public_b = power(g, private_b, p)

    shared_secret_a = power(public_b, private_a, p)
    shared_secret_b = power(public_a, private_b, p)

    return shared_secret_a, shared_secret_b

# Test the algorithm
if __name__ == "__main__":
    prime_modulus = int(input("Enter a prime modulus (p): "))
    generator = int(input("Enter a generator (g): "))
    private_key_a = int(input("Enter private key for user A: "))
    private_key_b = int(input("Enter private key for user B: "))
    
    shared_secret_a, shared_secret_b = diffie_hellman(prime_modulus, generator, private_key_a, private_key_b)
    
    print(f"Shared secret for user A: {shared_secret_a}")
    print(f"Shared secret for user B: {shared_secret_b}")
