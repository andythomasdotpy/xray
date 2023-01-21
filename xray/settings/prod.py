from decouple import config

from .base import *

print("prod")
SECRET_KEY = config("SECRET_KEY")
# HOSTED_ZONE_1 = config("HOSTED_ZONE_1")

DEBUG = False
ALLOWED_HOSTS = [
    "xray-env.eba-fczaaky6.us-west-2.elasticbeanstalk.com",
    "54.186.159.77",    
]

# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True