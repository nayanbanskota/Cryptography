def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(pk, cipher):
    d, n = pk
    plaintext = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plaintext)

# Test the RSA algorithm
if __name__ == "__main__":
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    plaintext = input("Enter the message to encrypt: ")
    
    public_key, private_key = generate_keypair(p, q)
    
    encrypted_text = encrypt(public_key, plaintext)
    decrypted_text = decrypt(private_key, encrypted_text)
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")
