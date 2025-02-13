from Crypto.Cipher import AES
import base64

key = b'Sixteen byte key'  # Key must be 16, 24, or 32 bytes long

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_message(encrypted_message):
    decoded = base64.b64decode(encrypted_message)
    nonce = decoded[:16]
    ciphertext = decoded[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()
