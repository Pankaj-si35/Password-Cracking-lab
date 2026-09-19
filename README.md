# Password-Cracking-lab
A hands-on cybersecurity lab demonstrating password hashing, dictionary attacks, Hashcat, John the Ripper, and password salting.
# Password Hashing & Dictionary Attack Lab

## Objective

This project demonstrates password hashing, dictionary-based password recovery in a controlled local lab environment, and the security benefits of salting.

## Tools Used

- Kali Linux
- Python 3
- Hashcat
- John the Ripper
- SHA-256
- PBKDF2
- Linux Terminal

## Practical Tasks

1. Generated a SHA-256 hash using Python.
2. Created a controlled test wordlist.
3. Performed a dictionary attack using Hashcat.
4. Tested password recovery using John the Ripper.
5. Implemented salted password hashing.
6. Compared unsalted and salted hashes.

## Security Concepts

### Password Hashing

Hashing converts a password into a fixed-length value. Password hashes should not be treated as encrypted passwords.

### Dictionary Attack

A dictionary attack tests candidate passwords from a wordlist against a target hash.

### Salting

A unique random salt makes identical passwords produce different hashes and makes precomputed hash attacks more difficult.

## Security Recommendations

- Do not store plaintext passwords.
- Use dedicated password-hashing algorithms such as Argon2id, bcrypt, scrypt, or PBKDF2.
- Use a unique random salt for every password.
- Never test against accounts or passwords without authorization.

## Disclaimer

This project was performed only in a controlled lab environment using test data for educational purposes.
