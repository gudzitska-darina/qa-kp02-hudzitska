class FileSystem:
    def __init__(self) -> None:
        pass

    class Directory:
        DIR_MAX_ELEMS = 100

        def __init__(self) -> None:
            pass

        def delete(self):
            pass

        def ls(self):
            pass

        def move(self, place):
            pass

    class BinaryFile:
        def __init__(self) -> None:
            pass

        def delete(self):
            pass

        def read(self) -> str:
            pass

        def move(self, place):
            pass

    class LogFile:
        def __init__(self) -> None:
            pass

        def delete(self):
            pass

        def read(self) -> str:
            pass

        def move(self, place):
            pass

        def append(self, item: str):
            pass

    class BufferFile:
        MAX_BUF_FILE_SIZE = 100

        def __init__(self) -> None:
            pass

        def delete(self):
            pass

        def push(self, item: str):
            pass

        def move(self, place):
            pass

        def consume(self):
            pass
