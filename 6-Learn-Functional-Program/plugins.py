from decorators import *


@configure_plugin_decorator
def configure_backups(path="~/backups", prefix="copy_", extension=".txt"):
    return {
        "path": path,
        "prefix": prefix,
        "extension": extension,
    }


@configure_plugin_decorator
def configure_login(user=None, password=None, token=None):
    return {
        "user": user,
        "password": password,
        "token": token,
    }
