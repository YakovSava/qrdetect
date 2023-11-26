from os import remove, listdir
from os.path import isfile, getsize, join

class Collector:

    def __init__(self, memory:int=1024*1024):
        self._memory = memory

    def _get_size(self, start_path:str=None) -> int:
        return sum(getsize(f) for f in listdir(start_path) if isfile(f))

    def forse_del_all(self, path:str=None) -> None:
        if self._get_size(path) >= self._memory:
            for file in listdir(path):
                if isfile(file):
                    remove(join(path, file))