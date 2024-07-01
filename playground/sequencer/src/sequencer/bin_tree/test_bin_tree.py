from .bin_tree import *

def test_converttolist():
    tree = NonEmptyBinTree(8,8,
        BranchNode(
            BranchNode(
                LeafNode(1),
                LeafNode(0),
            ),
            LeafNode(1),
        ),
    )
    assert list(tree) == [1,1,0,0,1,1,1,1]

def test_constructstree():
    array = [1,1,0,0,1,1,1,1,1,1,0,1]
    expected = NonEmptyBinTree(12,16,
        BranchNode(
            BranchNode(
                BranchNode(
                    LeafNode(1),
                    LeafNode(0),
                ),
                LeafNode(1),
            ),
            BranchNode(
                BranchNode(
                    LeafNode(1),
                    BranchNode(
                        LeafNode(0),
                        LeafNode(1),
                    ),
                ),
                LeafNode(1),
            ),
        ),
    )
    assert construct_bin_tree(array) == expected

def test_roundtrip():
    original = [1,1,0,1,1,0,0,0,0,1,1]
    bin_tree = construct_bin_tree(original)
    assert list(bin_tree) == original

def test_constructemptytree():
    assert construct_bin_tree([]) == EmptyBinTree()