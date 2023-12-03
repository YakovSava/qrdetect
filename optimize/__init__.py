from sys import platform
from os import listdir

if platform.startswith('linux'):
    if len(filter(lambda x: x.endswith('.so'), listdir('./cplugs/'))) != 2:
        LIBPATH = '/lib/python'
    from .cplugs.linfile import Bind
    from .cplugs.connector import Connector
elif platform == "win32":
    if len(filter(lambda x: x.endswith('.so'), listdir('./cplugs/'))) != 1:
        LIBPATH = ...
    from .cplugs.winfile import Bind

    from requests import get

    class Connector:

        def __init__(self):
            ...

        def connect(self, url:str) -> str:
            return get(url).text
else:
    raise ImportError('Platform not supported!')