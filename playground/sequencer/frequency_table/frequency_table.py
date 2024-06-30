from dataclasses import dataclass
from typing import Sequence
from ..utility import partition
from ..base_types import Bit

# Could type input as interface instead
def construct_frequency_table(input: Sequence[Bit]):

    # Copy input array as we will be modifying it
    n = len(input)
    array = list(input)
    subtables: list[list[Bit]] = []

    # Create subtables for each length smaller or equal to input length
    for s in range(1, len(input) + 1):
        subtable = [1 for _ in range(s)]

        # Partition array into ranges of size s
        # Perform "intersection" with each range to determine subtable
        for (start, stop) in partition(n, s):
            for i in range(start, stop):
                if array[i] == 0: subtable[i - start] = 0
        
        # If subtable is not empty, add to subtable list and "subtract" from array
        # Could potentially not iterate here
        if any(subtable):
            subtables.append(subtable)
            for (start, stop) in partition(n,s):
                for i in range(start, stop):
                    if subtable[i - start] == 1: array[i] = 0
    
    return FrequencyTable(subtables, length=n)

@dataclass
class FrequencyTable:

    # Sorted by subtable length (ascending)
    subtables: list[Sequence[Bit]]
    length: int

    def __getitem__(self, index) -> Bit:
        assert isinstance(index, int)
        # Raise IndexError for invalid indexes (this allows for loops to function properly)
        if index < 0 or index >= self.length: raise IndexError()
        for subtable in self.subtables:
            if subtable[index % len(subtable)] == 1: return 1
        return 0
    
    def __len__(self):
        return self.length