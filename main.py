from diary import diary

def main():
    d = diary("Diary_1")
    print("Diary made")
    d.add_entry("First", "First entry!")
    print("Entry made")
    d.rem_entry("First")
    print("Entry removed")
main()
