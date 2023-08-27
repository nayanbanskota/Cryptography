def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

# Test the function
if __name__ == "__main__":
    num = int(input("Enter a number to calculate Euler's Totient function: "))
    
    result = euler_totient(num)
    print(f"The Euler's Totient function value for {num} is {result}.")
