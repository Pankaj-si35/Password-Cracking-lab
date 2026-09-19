# 🔐 Password Hashing & Dictionary Attack Lab

A hands-on cybersecurity project demonstrating password hashing, controlled dictionary-based password recovery, salting, and password-security concepts using Kali Linux.

> **Educational Security Lab:** All testing in this project was performed against intentionally created test data in a controlled local environment. No real user accounts, credentials, or unauthorized systems were targeted.

---

## 📌 Project Overview

Passwords should never be stored in plaintext. Instead, secure applications store password representations using dedicated password-hashing mechanisms.

This project demonstrates how password hashes can be generated and how weak or predictable passwords can be identified through a controlled dictionary attack.

The project also demonstrates the importance of **unique salts** and computationally expensive password-hashing mechanisms for protecting stored credentials.

The practical implementation was performed using:

- Kali Linux
- Python 3
- Hashcat
- John the Ripper
- SHA-256
- PBKDF2
- Linux command-line tools

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand the difference between plaintext passwords and password hashes.
2. Generate cryptographic hashes using Python.
3. Create a controlled password wordlist.
4. Perform a dictionary attack against a self-generated test hash.
5. Use Hashcat for password recovery in a controlled lab.
6. Explore John the Ripper as an alternative password-auditing tool.
7. Understand the purpose of cryptographic salts.
8. Implement salted password hashing using Python.
9. Compare unsalted and salted hashing behavior.
10. Understand why fast general-purpose hashes are not ideal for password storage.
11. Practice documenting cybersecurity experiments professionally.

---

# 🧰 Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| Kali Linux | Security testing environment |
| Python 3 | Hash generation and cryptographic implementation |
| Hashcat | Dictionary-based password auditing |
| John the Ripper | Password auditing and recovery |
| SHA-256 | Cryptographic hashing demonstration |
| PBKDF2 | Password-based key derivation |
| Linux Terminal | Command-line execution |
| GitHub | Project documentation and portfolio |

---

# 🏗️ Project Workflow

The overall workflow of the project is:

```text
Test Password
      │
      ▼
Python Hash Generation
      │
      ▼
SHA-256 Hash
      │
      ▼
Store Test Hash
      │
      ▼
Controlled Wordlist
      │
      ▼
Dictionary Attack
      │
      ├───────────────┐
      ▼               ▼
   Hashcat       John the Ripper
      │               │
      └───────┬───────┘
              ▼
       Password Recovery
              │
              ▼
       Security Analysis
              │
              ▼
      Salted Hashing Demo
              │
              ▼
       PBKDF2 Implementation Practical Implementation
1. Hash Generation
A controlled test password was created for the laboratory environment.
Python's hashlib module was used to generate a SHA-256 digest.
Example:
import hashlib

password = "Cyber123"

sha256_hash = hashlib.sha256(
    password.encode()
).hexdigest()

print("Password:", password)
print("SHA-256:", sha256_hash)
The output is a fixed-length hexadecimal hash rather than the original plaintext password.
2. Hash Characteristics
SHA-256 produces a 256-bit digest represented as:
64 hexadecimal characters
A small change in the input produces a significantly different output.
For example:
Input A → Hash A

Input B → Completely different Hash B
This behavior is known as the avalanche effect.
3. Controlled Wordlist
A small test wordlist was created for the laboratory exercise.
Example:
password
123456
admin
letmein
Cyber123
Password123
Cyber2026
qwerty
The wordlist contains intentionally selected test passwords so that the password-auditing process can be demonstrated without targeting real credentials.
4. Dictionary Attack with Hashcat
Hashcat was used to perform a dictionary-based password recovery test against the self-generated SHA-256 hash.
Example command:
hashcat -m 1400 -a 0 hash.txt wordlist.txt
Where:
-m 1400
specifies SHA-256.
-a 0
specifies a straight/dictionary attack.
The attack compares candidate passwords from the controlled wordlist against the target test hash.
The result can be displayed using:
hashcat -m 1400 hash.txt --show
5. John the Ripper
John the Ripper was also explored as a password-auditing tool.
It provides another approach to testing password hashes against candidate passwords and demonstrates how multiple password-auditing tools can be used during authorized security assessments.
The exact command and hash format depend on the installed John the Ripper build and supported formats.
🧂 6. Salted Password Hashing
A major security concept demonstrated in this project is salting.
A salt is a randomly generated value added to a password before the password is processed by a password-hashing/KDF function.
Conceptually:
Password + Random Salt
          │
          ▼
   Password KDF / Hash
          │
          ▼
     Stored Result
For example:
Cyber123 + Salt_A → Hash_A

Cyber123 + Salt_B → Hash_B
Even though the password is identical, the resulting values are different because the salts are different.
7. PBKDF2 Implementation
Python was used to demonstrate PBKDF2 with SHA-256.
Example:
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
Running the program multiple times produces different salts and therefore different derived values. ⚠️ Important Security Analysis
A common misconception is:
"SHA-256 is secure, therefore SHA-256 is automatically suitable for storing passwords."
This is incorrect.
SHA-256 is a strong general-purpose cryptographic hash function, but it is designed to be fast.
For password storage, defenders generally want a password-hashing/KDF mechanism that is intentionally more computationally expensive and configurable.
Examples include:
Argon2id
bcrypt
scrypt
PBKDF2
The goal is to increase the cost of guessing large numbers of passwords while keeping legitimate authentication practical.
🛡️ Security Recommendations
For production applications:
1. Never store plaintext passwords
Do not store:
username: john
password: MyPassword123
Instead, store an appropriate password-hash representation.
2. Use a unique random salt
Each password should have its own cryptographically random salt.
3. Use a dedicated password-hashing algorithm
Prefer mechanisms designed for password storage, such as:
Argon2id
bcrypt
scrypt
PBKDF2
4. Use appropriate parameters
Password KDF parameters should be selected according to the application's security requirements and available computing resources.
5. Protect authentication infrastructure
Password security also depends on:
Rate limiting
MFA
Account lockout/risk controls
Secure session management
Breach detection
Strong password policies
Secure credential reset procedures
📸 Project Evidence
The repository contains screenshots demonstrating the practical execution of the project.
Evidence includes:
Hash generation
Wordlist creation
Hashcat execution
Password recovery in the controlled lab
Salted hashing implementation
Terminal outputs
Screenshots are provided for demonstration and verification of the practical work.
📁 Project Structure
Password-Cracking-Lab/
│
├── hash_demo.py
├── hash.txt
├── wordlist.txt
├── salted_hash.py
│
└── Screenshots/
    ├── hash-generation.png
    ├── hashcat-result.png
    ├── salted-hashing.png
    └── terminal-evidence.png
🧠 Key Learnings
Through this project, I gained practical experience with:
Linux security tooling
Cryptographic hashing
SHA-256
Password auditing
Dictionary attacks
Hashcat
John the Ripper
Salting
PBKDF2
Password-security weaknesses
Security documentation
Ethical security testing
🚧 Limitations
This project is intentionally designed as a small educational laboratory.
It does not represent a complete enterprise password-auditing environment.
Real-world password-security assessments may involve:
Large credential datasets
Multiple hash formats
GPU-based password auditing
Password-policy analysis
Credential exposure analysis
Authentication monitoring
Enterprise identity systems
Such activities require explicit authorization and appropriate safeguards.
⚖️ Ethical & Legal Disclaimer
This project was created strictly for cybersecurity education and authorized laboratory testing.
The password-auditing techniques demonstrated here should only be used against:
Your own systems
Your own test data
Explicitly authorized security-testing environments
CTF/lab environments where testing is permitted
Do not use these techniques to access, recover, or test passwords belonging to other people or systems without authorization.
🚀 Future Improvements
Possible future improvements include:
Implementing Argon2id
Building a password-strength analyzer
Adding secure password verification
Comparing Argon2id, bcrypt, scrypt, and PBKDF2
Building a small Flask authentication application
Adding automated security tests
Creating a password-hashing benchmark
Adding unit tests
Improving project documentation
Containerizing the lab environment
👨‍💻 Skills Demonstrated
Cybersecurity
Linux
Kali Linux
Password Security
Cryptography
Hashcat
John the Ripper
Python
SHA-256
PBKDF2
Salting
Dictionary Attacks
Security Testing
Technical Documentation
📌 Conclusion
This project demonstrates the practical relationship between password hashing, password auditing, salting, and secure password storage.
The laboratory shows why simply applying a fast cryptographic hash is not sufficient for password storage and why modern applications should use dedicated password-hashing/KDF mechanisms with unique salts and appropriate computational cost.
The project was performed entirely using controlled test data for educational and authorized cybersecurity practice. 
