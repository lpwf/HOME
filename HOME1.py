from pathlib import Path
from typing import List, Union, Iterator
import os


def get_files_list(path: str):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(os.path.join(path, file))
    return files


def merge_sorted_files(folder_path: str) -> Iterator:
    files_list = get_files_list(folder_path)
    nums = []
    for i in files_list:
        with open(file=i, encoding="utf-8", mode='r') as f:
            for row in f.readlines():
                try:
                    nums.append(int(row))
                except:
                    pass

    return iter(sorted(nums))