from celery import shared_task
from models.user import User
from models.user_history import UserHistory


@shared_task()
def user_history_task(data):
    user = User.objects(email=data.get("email")).first()
    action = data.get("action")
    user_history = UserHistory(user=user, action=action)
    user_history.save()
    return {"success": True, "message": "User history created successfully"}
