from directory import Directory


class BufferFile:
    MAX_BUF_FILE_SIZE = 100

    def __init__(self, name, max_elem, parent):
        if parent.DIR_MAX_ELEMS == len(parent.ls()):
            print('Parent directory is full')
            return

        self.name = name
        self.content = []
        self.MAX_BUF_FILE_SIZE = max_elem
        self.parent = parent

    def delete(self):
        del self
        print("Log file deleted successfully")
        return

    def push(self, item: str):
        self.content.append(item)

    def move(self, place):
        if place.DIR_MAX_ELEMS == len(place.content):
            print("Directory is full")
            return

        if type(place) is Directory:
            place.content.append(self)
            self.parent.content.remove(self)
            print("File transferred successfully")
        else:
            print("Directory with the given name was not found")

    def consume(self):
        return self.content.pop()
