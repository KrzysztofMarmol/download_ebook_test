from pathlib import Path


def ebooks_list_from_file():
    path = Path(__file__).parent / "Ebook_list.txt"
    with open(path, 'r') as file:
        return [line.rstrip() for line in file.readlines()]


