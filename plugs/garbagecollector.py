from os import remove, listdir
from os.path import isfile, getsize, join

class Collector:

    def __init__(self,
        kb_mem:int=0,
        mb_mem:int=0,
        gb_mem:int=0
    ):
        if gb_mem:
            self._memory = gb_mem * 1024 * 1024 * 1024
        elif mb_mem:
            self._memory = mb_mem * 1024 * 1024
        elif kb_mem:
            self._memory = kb_mem * 1024
        else:
            raise

    def _get_size(self, start_path:str=None) -> int:
        return sum(getsize(f) for f in listdir(start_path) if isfile(f))

    def forse_del_all(self, path:str=None) -> None:
        if self._get_size(path) >= self._memory:
            for file in listdir(path):
                if isfile(file):
                    remove(join(path, file))