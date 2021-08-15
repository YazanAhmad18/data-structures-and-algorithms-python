from trees import __version__

from trees.trees import  Binary_Tree, Node, Binary_Search_Tree

import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_an_empty_tree():
    b_tree=Binary_Search_Tree()
    actual=b_tree.root
    expected=None
    assert actual==expected

def  test_instantiate_tree_single_root_node():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.root.value
    expected=5
    assert actual==expected


    

   

def test_add_left_child_right_child_single_root():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=(tree.root.left.value,tree.root.right.value)
    expected=(3,8)
    assert actual==expected


def test_collection_from_preorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.pre_order()
    expected=[5,3,8]
    assert actual==expected

def test_collection_from_inorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.in_order()
    expected=[3,5,8]
    assert actual==expected


def test_collection_from_postorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.post_order()
    expected=[3,8,5]
    assert actual==expected




def test_max_val():
    b_tree=Binary_Search_Tree()
    b_tree.root=Node(2)
    b_tree.root.left=Node(5)
    b_tree.root.left.left=Node(6)
    b_tree.root.left.right=Node(9)
    b_tree.root.left.right.left=Node(1)
    b_tree.root.left.right.left=Node(4)
    b_tree.root.right=Node(3)
    b_tree.root.right.right=Node(7)
    b_tree.root.right.right.left=Node(12)


    actual=b_tree.max()
    expected=12
    assert actual==expected


    
