from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

def partition(stop: int, step: int) -> Generator[tuple[int,int], None, None]:
    index = 0
    while index < stop:
        prev_index = index
        index = min(index + step, stop)
        yield (prev_index, index)

def iter_pairs(iterable: Iterable[T]):
    it = iter(iterable)
    return zip(it, it)

__all__ = ["partition", "iter_pairs"]