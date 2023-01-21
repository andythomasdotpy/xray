from decouple import config

from .base import *

print("prod")
SECRET_KEY = config("SECRET_KEY")
# HOSTED_ZONE_1 = config("HOSTED_ZONE_1")

DEBUG = False
ALLOWED_HOSTS = [
    "xray-env.eba-fczaaky6.us-west-2.elasticbeanstalk.com",
    "127.0.0.1",    
]

# HTTPS settings
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# # HSTS settings
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False