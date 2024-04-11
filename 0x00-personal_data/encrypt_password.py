import bcrypt

def hash_password(password: str) -> bytes:
    """Hash the provided password using bcrypt."""
    # Generate a salt and hash the password using bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    # Use bcrypt to verify the password against the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
