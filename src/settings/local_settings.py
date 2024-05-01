import os

from dotenv import load_dotenv
load_dotenv('.env')


DEBUG = True
LOG_ROOT = os.getenv("LOG_ROOT")
LOG_FILENAME = "{}.log".format(os.getenv("APPLICATION_NAME"))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "default",
            "encoding": "utf-8",
            "filename": os.path.join(LOG_ROOT, LOG_FILENAME),
        }
    },
    "loggers": {
        "default": {
            "handlers": ["default"],
            "level": "DEBUG",
            "propogate": True,
        }
    },
}


MONGO_SETTINGS = {
    "DB_NAME": os.getenv("DB_NAME"),
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_PORT": int(os.getenv("DB_PORT", 27017)),
    "DB_USERNAME": os.getenv("DB_USERNAME"),
    "DB_PASSWORD": os.getenv("DB_PASSWORD"),
}
