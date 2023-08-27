def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    if gcd(g, p) != 1:
        return False
    
    phi_p = p - 1  # Euler's Totient function for prime p
    powers = set()

    for i in range(1, phi_p + 1):
        powers.add(pow(g, i, p))
    
    return len(powers) == phi_p

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Test the program
if __name__ == "__main__":
    modulus = int(input("Enter a prime modulus: "))
    
    primitive_root = find_primitive_root(modulus)
    if primitive_root is not None:
        print(f"A primitive root modulo {modulus} is {primitive_root}.")
    else:
        print(f"No primitive root found for modulo {modulus}.")
