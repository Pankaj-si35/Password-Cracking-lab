import hashlib

password = "Cyber123"

sha256_hash = hashlib.sha256(password.encode()).hexdigest()

print("Password:", password)
print("SHA-256:", sha256_hash)
