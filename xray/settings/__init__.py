from decouple import config

try:
    SETTINGS_VAR = config("SETTINGS_DEV_PROD")
    print(SETTINGS_VAR)
    if SETTINGS_VAR == "prod":
        from .prod import *
except:
        from .dev import *