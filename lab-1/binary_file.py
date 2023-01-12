from directory import Directory


class BinaryFile:
    def __init__(self, name, parent):
        if parent.DIR_MAX_ELEMS == len(parent.ls()):
            print('Parent directory is full')
            return

        self.name = name
        self.content = ""
        self.parent = parent

    def delete(self):
        del self
        print("Binary file deleted successfully")
        return

    def read(self):
        print(self.content)

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
