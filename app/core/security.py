from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plainpassword):
    return bcrypt_context.hash(plainpassword)

def verify_password(plainpassword, hashedpassword):
    return bcrypt_context.verify(plainpassword, hashedpassword)