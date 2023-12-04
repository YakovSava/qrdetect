from sys import platform
from os import listdir, popen

if platform.startswith('linux'):
    if "aarch" in popen("lscpu | grep Architecture").read():
        raise Exception("ARM not supported!")
    if len(filter(lambda x: x.endswith('.so'), listdir('./cplugs/'))) != 2:
        LIBPATH = '/lib/python'
    from .cplugs.linfile import Bind
    from .cplugs.connector import Connector
elif platform == "win32":
    if len(filter(lambda x: x.endswith('.pyd'), listdir('./cplugs/'))) != 1:
        LIBPATH = ...
    from .cplugs.winfile import Bind

    from requests import get

    class Connector:

        def __init__(self):
            self._reqc = 0

        def connect(self, url:str) -> str:
            self._reqc += 1
            return get(url).text
            
        def reqcount(self) -> int:
            return self._reqc
else:
    raise ImportError('Platform not supported!')