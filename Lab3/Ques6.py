import random
from sympy import mod_inverse

def generate_keypair():
    p = 23
    g = find_primitive_root(p)
    a = random.randint(2, p - 2)
    A = pow(g, a, p)

    return (p, g, a), A

def encrypt(public_key, plaintext):
    p, g, A = public_key
    k = random.randint(2, p - 2)
    B = pow(g, k, p)
    s = pow(A, k, p)
    ciphertext = (pow(g, k, p), (plaintext * s) % p)

    return ciphertext, B

def decrypt(private_key, ciphertext):
    p, _, a = private_key
    alpha, beta = ciphertext
    s = pow(alpha, a, p)
    s_inv = mod_inverse(s, p)
    plaintext = (beta * s_inv) % p

    return plaintext

def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // i, p) != 1 for i in range(2, int((p - 1) ** 0.5) + 1)):
            return g

if __name__ == "__main__":
    private_key, public_key = generate_keypair()
    print("Private Key:", private_key)
    print("Public Key:", public_key)

    message = 7
    print("Original Message:", message)
    ciphertext, ephemeral_public_key = encrypt(public_key, message)
    print("Encrypted Message:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted Message:", decrypted_message)
