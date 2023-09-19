import os


class EntryAlreadyExists(Exception):
    pass


class NoEntryFound(Exception):
    pass


class diary:
    def __init__(self, diaryname):
        self.diaryname = diaryname
        if not os.path.exists(diaryname):
            os.makedirs(diaryname)

    def add_entry(self, title, content):
        if os.path.exists(self.diaryname + "/" + title + ".txt"):
            raise EntryAlreadyExists("Entry already exists")
        else:
            file = open(self.diaryname + "/" + title + ".txt", "w")
            file.write(content)
            file.close()

    def rem_entry(self, title):
        if os.path.exists(self.diaryname + "/" + title + ".txt"):
            os.remove(self.diaryname + "/" + title + ".txt")
        else:
            raise NoEntryFound("That entry doesn't exists")

    def read_entry(self, title):
        if os.path.exists(self.diaryname + "/" + title + ".txt"):
            file = open(self.diaryname + "/" + title + ".txt", "r")
            print(file.read())
            file.close()
        else:
            raise NoEntryFound("That entry doesn't exist")
