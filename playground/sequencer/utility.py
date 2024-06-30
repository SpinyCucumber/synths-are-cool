from typing import Generator

def partition(stop: int, step: int) -> Generator[tuple[int,int], None, None]:
    index = 0
    while index < stop:
        prev_index = index
        index = min(index + step, stop)
        yield (prev_index, index)