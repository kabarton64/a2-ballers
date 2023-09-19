from diary import diary


def main():
    d = diary("Diary_1")
    print("Diary made")
    d.add_entry("Jan. 01 2023", "First entry!")
    print("Entry made")
    d.rem_entry("Jan. 01 2023")
    print("Entry removed")


main()
