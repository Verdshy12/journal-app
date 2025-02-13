import bcrypt

# Hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Verify a password
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)
