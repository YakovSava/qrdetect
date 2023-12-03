from sys import platform
from os import listdir

if platform.startswith('linux'):
    if len(filter(lambda x: x.endswith('.so'), listdir())) != 2:
        LIBPATH = '/lib/python'
    from linfile import Bind
    from connector import Connector
elif platform == "win32":
    if len(filter(lambda x: x.endswith('.so'), listdir())) != 1:
        LIBPATH = ...
    from winfile import Bind

    from requests import get

    class Connector:

        def __init__(self):
            ...

        def connect(self, url:str) -> str:
            return get(url).text
else:
    raise ImportError('Platform not supported!')