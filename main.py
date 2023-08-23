from pathlib import Path
from typing import List

from Trie import Trie


def read_file(file_path: str, t: Trie):
    with open(file_path, 'r', encoding='utf-8') as f:
        filename = Path(f.name).name
        for line in f.readlines():
            t.insert(line, filename)


def get_iterator_of_files(files_path: str = r"Archive"):
    return list(Path(files_path).rglob("*.txt"))


def init():
    files_it = get_iterator_of_files()
    tree = Trie()
    for file in files_it:
        read_file(file, tree)


def main():
    init()


if __name__ == '__main__':
    main()
