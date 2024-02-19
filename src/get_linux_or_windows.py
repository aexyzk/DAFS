import os

def isLinux():
    if os.name == "nt":
        _isLinux = False
    else:
        _isLinux = True

    return _isLinux