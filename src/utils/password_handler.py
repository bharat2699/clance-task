import bcrypt


class PasswordHandler:
    def __init__(self):
        pass

    def hash_password(self, password) -> str:
        if not password:
            return None
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password.decode("utf-8")

    def is_password_valid(self, password, hashed_password) -> bool:
        if not password or not hashed_password:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
