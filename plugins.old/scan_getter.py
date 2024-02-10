class ScanGetter:

    def __init__(self, from_filename:str):
        self._from = from_filename

    def _get_all(self) -> list[str]:
        with open(self._from, 'r', encoding='utf-8') as file:
            return file.readlines()

    def get_last(self) -> str:
        return self._get_all()[-1]

    def get_slice(self, slice:int) -> list[str]:
        return self._get_all()[-slice:]