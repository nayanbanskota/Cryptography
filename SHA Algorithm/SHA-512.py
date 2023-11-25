import hashlib

class SHA512Hasher:
    def __init__(self, data=None):
        self.sha512_hash = hashlib.sha512()
        if data:
            self.update(data)

    def update(self, data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.sha512_hash.update(data)

    def hexdigest(self):
        return self.sha512_hash.hexdigest()

def sha512_hash(data):
    """
    Generate the SHA-512 hash of the given data.

    Parameters:
    - data (str or bytes): The input data to be hashed.

    Returns:
    - str: The hexadecimal representation of the SHA-512 hash.
    """
    hasher = SHA512Hasher(data)
    return hasher.hexdigest()

# Example usage:
if __name__ == "__main__":
    data_to_hash = "Hello, SHA-512!"
    hashed_result = sha512_hash(data_to_hash)
    print(f"Input: {data_to_hash}")
    print(f"SHA-512 Hash: {hashed_result}")
