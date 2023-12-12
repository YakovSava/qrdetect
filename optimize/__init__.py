from sys import platform
from os import listdir, system, popen

system('python3 cplugs/comp.py build_ext --inplace')

if platform.startswith('linux'):
    if "aarch" in popen("lscpu | grep Architecture").read():
        raise Exception("ARM not supported!")
    from .cplugs.linfile import Bind
    from .cplugs.connector import Connector
elif platform == "win32":
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