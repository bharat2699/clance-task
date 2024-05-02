from choices import StatusCodes, UserHistoryAction
from models.user import User
from services.base_service import BaseService
from tasks.user_history_tasks import user_history_task
from utils.password_handler import PasswordHandler


class UserService(BaseService):
    def __init__(self):
        self.ph = PasswordHandler()

    def signup_user(self, data):
        try:
            existing_user = User.objects(email=data.get("userEmail")).first()
            if existing_user:
                return self.exception(
                    {
                        "success": False,
                        "code": StatusCodes().BAD_REQUEST,
                        "errors": "User already exists",
                    },
                    StatusCodes().BAD_REQUEST,
                )
            name = data.get("userName")
            email = data.get("userEmail")
            password = data.get("userPassword")
            create_user = User(name=name, email=email, password=password)
            create_user.save()
            history_task = user_history_task.delay(
                {"email": email, "action": UserHistoryAction().SIGNUP}
            )
            return self.ok(
                {
                    "success": True,
                    "code": StatusCodes().CREATED,
                    "data": {
                        "id": str(create_user.id),
                        "name": create_user.name,
                        "email": create_user.email,
                    },
                    "message": "User created successfully",
                },
                StatusCodes().CREATED,
            )
        except Exception as e:
            return self.exception(
                {
                    "success": False,
                    "code": StatusCodes().ISE,
                    "errors": str(e),
                },
                StatusCodes().ISE,
            )

    def login_user(self, data):
        try:
            user = User.objects(email=data.get("userEmail")).first()
            if not user:
                return self.exception(
                    {
                        "success": False,
                        "code": StatusCodes().NOT_FOUND,
                        "errors": "User not found",
                    },
                    StatusCodes().NOT_FOUND,
                )
            if (
                self.ph.is_password_valid(data.get("userPassword"), user.password)
                is False
            ):
                return self.exception(
                    {
                        "success": False,
                        "code": StatusCodes().UNAUTHORIZED,
                        "errors": "Invalid password",
                    },
                    StatusCodes().UNAUTHORIZED,
                )
            history_task = user_history_task.delay(
                {"email": user.email, "action": UserHistoryAction().LOGIN}
            )
            return self.ok(
                {
                    "success": True,
                    "code": StatusCodes().SUCCESS,
                    "data": {
                        "id": str(user.id),
                        "name": user.name,
                        "email": user.email,
                    },
                    "message": "User logged in successfully",
                },
                StatusCodes().SUCCESS,
            )
        except Exception as e:
            return self.exception(
                {
                    "success": False,
                    "code": StatusCodes().ISE,
                    "errors": str(e),
                },
                StatusCodes().ISE,
            )
