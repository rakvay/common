from cryptography.fernet import Fernet

# generate a key
key = Fernet.generate_key()
print('Generated key(AES):', key)

# encrypt the data using the Fernet object
f = Fernet(key)
message = b"Secrets go here"
encrypted = f.encrypt(message)
f = Fernet(key)
print(f.decrypt(encrypted))
