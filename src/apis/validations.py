from marshmallow import Schema, fields, validate


class SignUpSchema(Schema):
    userName = fields.Str(
        required=True,
        error_messages={
            "required": "Name is required.",
            "null": "Name cannot be null.",
        },
        nullable=False,
        validate=validate.Length(
            min=3, max=200, error="Name must be between 3 and 200 characters."
        ),
    )
    userEmail = fields.Email(
        nullable=False,
        required=True,
        error_messages={
            "required": "Email is required.",
            "null": "Name cannot be null.",
            "invalid": "Invalid email.",
        },
    )
    userPassword = fields.Str(
        required=True,
        nullable=False,
        error_messages={
            "required": "Password is required.",
            "null": "Password cannot be null.",
        },
        validate=validate.Length(
            min=3, max=8, error="Password must be between 3 and 8 characters."
        ),
    )


class LoginSchema(Schema):
    userEmail = fields.Email(
        nullable=False,
        required=True,
        error_messages={
            "required": "Email is required.",
            "null": "Name cannot be null.",
            "invalid": "Invalid email.",
        },
    )
    userPassword = fields.Str(
        required=True,
        nullable=False,
        error_messages={
            "required": "Password is required.",
            "null": "Password cannot be null.",
        },
        validate=validate.Length(
            min=3, max=8, error="Password must be between 3 and 8 characters."
        ),
    )
