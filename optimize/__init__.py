from sys import platform
from os import listdir, system, popen

system('python3 cplugs/comp.py build_ext --inplace')

if platform.startswith('linux'):
    if "aarch" in popen("lscpu | grep Architecture").read():
        raise Exception("ARM not supported!")
    from .cplugs.linfile import read, write
elif platform == "win32":
    from .cplugs.winfile import read, write
else:
    raise ImportError('Platform not supported!')