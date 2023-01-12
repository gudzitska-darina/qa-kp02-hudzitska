class Directory:
    DIR_MAX_ELEMS = 0

    def __init__(self, name, max_count_elems, parent = None):
        # if not type(parent) == None:
        #     if parent.DIR_MAX_ELEMS == len(parent.content):
        #         print('Parent directory is full')
        #         return

        self.name = name
        self.DIR_MAX_ELEMS = max_count_elems
        self.content = []
        self.parent = parent
        if parent is not None:
            parent.content.append(self)

    def delete(self):
        del self
        print("Directory deleted successfully")
        return

    def ls(self):
        print(f"{self.name}:\r\n")
        for elem in self.content:
            if type(elem) is Directory:
                Directory(elem).ls()
            print(f"|{elem.name}|")

    def move(self, moved_file, place):
        if place.DIR_MAX_ELEMS == len(place.content):
            print("Directory is full")
            return

        if type(place) is Directory:
            place.content.append(moved_file)
            moved_file.parent = place
            self.content.remove(moved_file)
            print("File transferred successfully")
        else:
            print("Directory with the given name was not found")
