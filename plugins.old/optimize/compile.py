from sys import platform, executable
from os import system

class NoCompilerError(Exception): pass

if platform.startswith("linux"):
    not_found_status = 32512
    error_status = 1
elif platform == "win32":
    not_found_status = 1
    error_status = 1
else:
    raise RuntimeError("Platform not supported")

if system("gcc") == not_found_status:
    raise NoCompilerError("GCC not found")
elif system("g++") == not_found_status:
    raise NoCompilerError("G++ not found")
if platform == "win32":
    if system("fasm") == not_found_status:
        raise NoCompilerError("FASM not found")

if platform == "win32":
    pylibs = ...
    pyinclude = ...
else:
    pylibs = ...
    pyinclude = ...

compile_args = [...]

def _compile():
    system(...)

if __name__ == '__main__':
    _compile()