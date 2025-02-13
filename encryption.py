from cryptography.fernet import Fernet

# Generate a key (Do this once and save it securely)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the stored key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a message
def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

# Run only once to generate a key
# generate_key()
