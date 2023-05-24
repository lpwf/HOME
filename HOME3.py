from pathlib import Path
from typing import Optional, Callable
import os


def universal_file_counter(
        dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    line_count = 0
    token_count = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if tokenizer is None:
                        line_count += len(f.readlines())
                    else:
                        tokens = tokenizer(f.read())
                        token_count += len(tokens)
    if tokenizer is None:
        return line_count
    else:
        return token_count