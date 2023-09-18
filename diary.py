import os

class diary:
    def __init__(self, diaryname):
        self.diaryname = diaryname
        if not os.path.exists(diaryname):
            os.makedirs(diaryname)

    def add_entry(self, title, content):
        file = open(self.diaryname + "/" + title + ".txt", "w")
        file.write(content)
        file.close()

    def rem_entry(self, title):
        os.remove(self.diaryname + "/" + title + ".txt")
