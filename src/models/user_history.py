from mongoengine import Document, ReferenceField, IntField, DateTimeField
from .user import User
from datetime import datetime, timezone


class UserHistory(Document):
    user = ReferenceField(User, required=True)
    action = IntField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
