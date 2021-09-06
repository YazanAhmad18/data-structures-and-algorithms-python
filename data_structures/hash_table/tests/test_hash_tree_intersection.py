from hash_table import __version__
from hash_table.hash_tree_intersection import tree_intersection
from hash_table.trees import Binary_Tree,Node


def test_one():
    first_tree=Binary_Tree()
    first_tree.root=Node(90)
    first_tree.root.left=Node(75)
    first_tree.root.left.left=Node(10)
    first_tree.root.right=Node(280)
    first_tree.root.left.right=Node(11)
    first_tree.root.right.left=Node(170)

    second_tree=Binary_Tree()
    second_tree.root=Node(90)
    second_tree.root.left=Node(66)
    second_tree.root.right=Node(22)
    second_tree.root.left.left=Node(280)
    second_tree.root.left.left.right=Node(13)
    second_tree.root.right.right=Node(170)
    actual= tree_intersection(first_tree, second_tree)
    expected=[90,280,170]
    assert actual == expected


def test_two():
    first_tree=Binary_Tree()
    first_tree.root=Node(80)
    first_tree.root.left=Node(50)
    first_tree.root.left.left=Node(36)
    first_tree.root.left.left.left=Node(10)
    first_tree.root.right=Node(70)

    second_tree=Binary_Tree()
    second_tree.root=Node(100)
    second_tree.root.left=Node(50)
    second_tree.root.left.left=Node(36)
    second_tree.root.left.left.left=Node(13)
    second_tree.root.right=Node(70)
    actual= tree_intersection(first_tree,second_tree)
    expected=[50,36,70]
    assert actual == expected


def test_tree_empty():
    first_tree=Binary_Tree()
    second_tree=Binary_Tree()
    actual= tree_intersection(first_tree,second_tree)
    expected='one of the trees is empty'
    assert actual == expected

def test_tree_no_intersection():
    frist_tree=Binary_Tree()
    frist_tree.root=Node(12)
    frist_tree.root.right=Node(17)
    frist_tree.root.left=Node(62)
    frist_tree.root.left.left=Node(67)
    frist_tree.root.right.right=Node(200)

    second_tree=Binary_Tree()
    second_tree.root=Node(92)
    second_tree.root.left=Node(105)
    second_tree.root.left.left=Node(117)
    second_tree.root.left.left.left=Node(18)
    second_tree.root.left.right=Node(22)
    actual= tree_intersection(frist_tree,second_tree)
    expected='input Trees there is not intersection'
    assert actual == expected







