from dataclasses import dataclass
from typing import Protocol, Sequence
from math import ceil, log2, pow
from ..base_types import Bit
from ..utility import iter_pairs

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
        if index < c: return self.left.get_value(index, c)
        return self.right.get_value(index - c, c)

@dataclass
class NonEmptyBinTree:

    length: int
    """Size of tree. Must be power of 2."""
    size: int
    root: Node

    def __getitem__(self, index):
        assert isinstance(index, int)
        # Raise IndexError for invalid indexes (this allows for loops to function properly)
        if index < 0 or index >= len(self): raise IndexError()
        return self.root.get_value(index, self.size)
    
    def __len__(self):
        return self.length

# Awkward case where input list has no elements
@dataclass
class EmptyBinTree:

    def __getitem__(self, _index):
        raise IndexError()

    def __len__(self):
        return 0

BinTree = NonEmptyBinTree | EmptyBinTree

def construct_bin_tree(input: Sequence[Bit]) -> BinTree:

    n = len(input)
    if (n == 0): return EmptyBinTree()
    
    # "Extend" input array so that length matches next power of 2
    order = ceil(log2(n))
    size = int(pow(2,order))
    extended_input = list(input) + ((size - n) * [input[-1]])

    # Create initial array of nodes (each node is leaf node)
    nodes = [LeafNode(value) for value in extended_input]

    # Repeatedly *merge* pairs of nodes until we are left with single node
    def merge_pairs(to_merge: list[LeafNode | BranchNode]):
        return [
            left if (isinstance(left, LeafNode) and isinstance(right, LeafNode) and (left.value == right.value)) else BranchNode(left, right)
            for left, right in iter_pairs(to_merge)
        ]
    
    for _ in range(order):
        nodes = merge_pairs(nodes)
    
    return NonEmptyBinTree(n, size, nodes[0])

__all__ = ["Node", "BranchNode", "LeafNode", "NonEmptyBinTree", "EmptyBinTree", "BinTree", "construct_bin_tree"]