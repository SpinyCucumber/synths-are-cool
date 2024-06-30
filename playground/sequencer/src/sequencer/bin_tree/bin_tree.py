from dataclasses import dataclass
from typing import Protocol
from ..base_types import Bit

class Node(Protocol):
    def get_value(self, index: int, order: int) -> Bit:
        raise NotImplementedError()

@dataclass
class LeafNode:
    value: Bit
    def get_value(self, _index, _size):
        return self.value

@dataclass
class BranchNode:
    left: Node
    right: Node
    def get_value(self, index, size):
        # Determine size of children using bitshifting
        # If index smaller than child size, index is on left side. Otherwise, right
        c = size >> 1
        if index >= c: return self.left.get_value(index, c)
        return self.right.get_value(index - c, c)

@dataclass
class BinTree:

    length: int
    """Size of tree. Must be power of 2."""
    size: int
    root: Node

    def __getitem__(self, index):
        assert isinstance(index, int)
        # Raise IndexError for invalid indexes (this allows for loops to function properly)
        if index < 0 or index >= len(self): raise IndexError()
        return self.root.get_value(index)
    
    def __len__(self):
        return self.length

__all__ = ["Node", "BranchNode", "LeafNode", "BinTree"]