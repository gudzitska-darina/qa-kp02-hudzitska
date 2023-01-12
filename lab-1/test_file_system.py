
from directory import Directory
from binary_file import BinaryFile
from log_file import LogFile
from buffer_file import BufferFile


class TestDirectory:
    def test_init(self):
        name = "Main"
        max_num_elem = 10
        test_directory = Directory(name, max_num_elem)

        assert test_directory.name == name
        assert len(test_directory.content) == 0
        assert type(test_directory) is not None

    def test_content_list(self):
        directory = Directory("main", 10)

        assert type(directory.content) is list

        directory.content.append("logs")

        assert len(directory.content) == 1
        assert type(directory.content[0]) is str

    def test_move_directory(self):
        main_dir = Directory("main", 10)
        inner_dir = Directory("inner", 10, main_dir)
        moved_dir = Directory("test1", 10, inner_dir)

        assert len(main_dir.content) == 1
        assert len(inner_dir.content) == 1
        assert moved_dir.parent == inner_dir

        inner_dir.move(moved_dir, main_dir)

        assert len(main_dir.content) == 2
        assert len(inner_dir.content) == 0
        assert moved_dir.parent == main_dir

    def test_del_directory(self):
        test_dir = Directory("test", 10)

        assert test_dir.delete() is None


class TestBinaryFile:
    directory = Directory("main", 10)

    def test_init(self):
        name = "bin"
        binar = BinaryFile(name, self.directory)

        assert binar is not None
        assert len(self.directory.content) == 1

    def test_move(self):
        binar = BinaryFile("bin_file", self.directory)
        directory_for_move = Directory("move", 10)

        binar.move(directory_for_move)

        assert len(directory_for_move.content) == 1

    def test_read(self):
        text = "fnvskjvkdfbvbdk"
        binar = BinaryFile("bin_file", self.directory)
        binar.content = text

        assert len(binar.content) != 0
        assert type(binar.content) is str

    def test_del(self):
        binar = BinaryFile("bin_file", self.directory)

        assert binar.delete() is None


class TestBufferFile:
    directory = Directory("main", 10)

    def test_init(self):
        name = "buff_file"
        max_elem = 6
        test_buff = BufferFile(name, max_elem, self.directory)

        assert test_buff is not None
        assert test_buff.MAX_BUF_FILE_SIZE == max_elem
        assert len(self.directory.content) == 1

    def test_move(self):
        buff = BufferFile("buff_file", 7, self.directory)
        directory_for_move = Directory("move", 10)

        buff.move(directory_for_move)

        assert len(directory_for_move.content) == 1

    def test_push_elem(self):
        text1 = "first"
        text2 = "second"
        buff = BufferFile("buff_file", 7, self.directory)

        buff.push(text1)
        buff.push(text2)

        assert len(buff.content) == 2
        assert buff.content.pop() == text2

    def test_del(self):
        buff = BufferFile("buff_file", 7, self.directory)

        assert buff.delete() is None


class TestLogFile:
    directory = Directory("main", 10)

    def test_init(self):
        name = "log_file"
        test_log = LogFile(name, self.directory)

        assert test_log is not None
        assert len(self.directory.content) == 1

    def test_read(self):
        text = "log text"
        log = LogFile("log_file", self.directory)
        log.content = text

        assert len(log.content) != 0
        assert type(log.content) is str

    def test_append_new_content(self):
        text = "log text"
        log = LogFile("log_file", self.directory)
        log.content = text

        new_text = "new text"
        log.append(new_text)

        assert len(log.content) != 0
        assert type(log.content) is str
        assert log.content[-1] == new_text[-1]

    def test_move(self):
        log = LogFile("log_file", self.directory)
        directory_for_move = Directory("move", 10)

        log.move(directory_for_move)

        assert len(directory_for_move.content) == 1

    def test_del(self):
        log = LogFile("log_file", self.directory)

        assert log.delete() is None
