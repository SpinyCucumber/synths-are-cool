from dataclasses import dataclass
from typing import Sequence
from ..base_types import Bit

INITIAL_VALUE = 1

@dataclass
class RunList:
    
    # Zero can also be used to start list of 0 instead of 1
    run_stops: list[int]

    def __getitem__(self, index) -> Bit:
        assert isinstance(index, int)
        # Raise IndexError for invalid indexes (this allows for loops to function properly)
        if index < 0 or index >= self.run_stops[-1]: raise IndexError()
        # Run implicitly starts ON (1)
        # After each run, value is toggled
        value = INITIAL_VALUE
        for run_stop in self.run_stops:
            if index < run_stop: return value
            value = int(not value)
    
    def __len__(self):
        return self.run_stops[-1]

def construct_run_list(input: Sequence[Bit]):
    n = len(input)
    value = INITIAL_VALUE
    run_stops: list[int] = []
    # Create run for each change in input array
    for i in range(n):
        if value != input[i]:
            run_stops.append(i)
            value = input[i]
    # Final run
    run_stops.append(n)
    return RunList(run_stops)

__all__ = ["RunList", "construct_run_list"]