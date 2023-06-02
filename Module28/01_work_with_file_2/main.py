
class File:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file = None

    def __enter__(self) -> object:
        try:
            self.file = open(self.file_name, 'r', encoding='utf8')
        except FileNotFoundError:
            self.file = open(self.file_name, 'x', encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.file:
            self.file.close()
        return True


with File("test_reading.txt") as file:
    file.write("Всем привет!")
    print(file.read())

with File("test_writing.txt") as file:
    file.write("Всем привет!")
    print(file.read())

