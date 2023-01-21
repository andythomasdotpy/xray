from decouple import config

try:
    if config("SETTINGS_DEV_PROD") == "prod":
        from .prod import *
except:
    from .dev import *