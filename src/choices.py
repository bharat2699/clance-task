from dataclasses import dataclass


@dataclass
class StatusCodes(object):
    def __init__(self):
        self.SUCCESS = 200
        self.CREATED = 201
        self.NO_CONTENT = 204
        self.BAD_REQUEST = 400
        self.UNAUTHORIZED = 401
        self.FORBIDDEN = 403
        self.NOT_FOUND = 404
        self.UNPROCESSABLE_ENTITY = 422
        self.ISE = 500
        self.BAD_GATEWAY = 502
        self.SERVICE_UNAVAILABLE = 503


obj_status_codes = StatusCodes()
StatusCodesDictionary = obj_status_codes.__dict__


@dataclass
class UserHistoryAction(object):
    def __init__(self):
        self.SIGNUP = 1
        self.LOGIN = 2


obj_user_history_action = UserHistoryAction()
UserHistoryActionDictionary = obj_user_history_action.__dict__
