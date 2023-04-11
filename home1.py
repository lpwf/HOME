"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

from collections import Counter
from typing import List
import re


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding='utf-8', mode='r') as fi:
        text = fi.read().encode('utf-8').decode('unicode-escape')
        words = text.split(' ')
        finale_list = sorted(words, key=lambda x: len(set(x)), reverse=True)
        finale_list = finale_list[:10]

    return finale_list


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding='utf-8', mode='r') as file:
        counter = Counter(
            file.read().encode('utf-8').decode('unicode-escape'))  # Searches for the rarest symbol, including case
    rarest_symbol = min(counter, key=counter.get)
    return rarest_symbol


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding='utf-8', mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        string_without_letter = re.sub(r'[^!.,?:;\-\(\)\"\"]', '', text)
        punctuation_char = len(string_without_letter)
        return punctuation_char


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        a = 0
        for i in text:
            if i.isascii():  # Non-ascii character
                a += 1
        return a


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        ascii_char = ''
        for i in text:
            if not i.isascii():  # Searches for a frequently occurring non-ascii symbol
                ascii_char += i
        counter = Counter(ascii_char)
        most_common_symbol = max(counter, key=counter.get)
        return most_common_symbol
