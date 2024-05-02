from mongoengine import Document, StringField, EmailField, DateTimeField
from utils.password_handler import PasswordHandler
from datetime import datetime, timezone

ph = PasswordHandler()


class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.password = ph.hash_password(self.password)
        super(User, self).save(*args, **kwargs)
