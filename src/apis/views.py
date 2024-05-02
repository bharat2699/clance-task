import logging
from flask import request, jsonify
from apis.validations import LoginSchema, SignUpSchema
from choices import StatusCodes
from services.user_service import UserService


logger = logging.getLogger("default")
service = UserService()


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def signup():
    data = request.json
    schema = SignUpSchema()
    try:
        validated_data = schema.load(data)
    except Exception as e:
        return jsonify(e.messages), StatusCodes().UNPROCESSABLE_ENTITY
    service_data = service.signup_user(validated_data)
    if "errors" in service_data:
        return jsonify(service_data["errors"]), service_data["code"]
    return (
        jsonify(service_data["response_data"]),
        StatusCodes().CREATED,
    )


def login():
    data = request.json
    schema = LoginSchema()
    try:
        validated_data = schema.load(data)
    except Exception as e:
        return jsonify(e.messages), StatusCodes().UNPROCESSABLE_ENTITY
    service_data = service.login_user(validated_data)
    if "errors" in service_data:
        return jsonify(service_data["errors"]), service_data["code"]
    return (
        jsonify(service_data["response_data"]),
        StatusCodes().SUCCESS,
    )
