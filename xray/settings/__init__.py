settings = "dev"

if settings == "prod":
    from .prod import *
else:
    from .dev import *