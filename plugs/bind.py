def read(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write(filename: str, data: str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
