from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

hashed = pwd_context.hash("admin123")
# print(hashed)
result = pwd_context.verify(
    "admin",
    hashed
)
print(result)