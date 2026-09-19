import hashlib
import secrets

password = "Cyber123"

salt = secrets.token_bytes(16)

hashed_password = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    100000
)

print("Password:", password)
print("Salt:", salt.hex())
print("Hash:", hashed_password.hex())
