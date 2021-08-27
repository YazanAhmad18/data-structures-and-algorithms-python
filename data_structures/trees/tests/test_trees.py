from trees import __version__

from trees.trees import  Binary_Tree, Node, Binary_Search_Tree
from trees.k_ary_tree import k_Node,tree_fizz_buzz,k_ary 



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


def test_breadth_first():
    tree = Binary_Tree()
    tree.root=Node(1)
    tree.root.left=Node(3)
    tree.root.right=Node(7)
    tree.root.left.left=Node(2)
    tree.root.left.right=Node(4)
    tree.root.right.right=Node(6)
    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(7)

    actual = tree.breadth_first()
    expected = [1,3,7,2,4,6,5,7]

    assert actual == expected

    
def test_fizz_buzz_tree_empty():
    t = Binary_Tree()
    actual = t.fizz_buzz_tree()
    expected = "tree is Empty"
    assert actual == expected


def test_fizz_buzz_tree():
    tree = Binary_Tree()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(5)
    tree.root.left.right=Node(7)
    tree.root.right.right=Node(9)
    tree.root.left.right.left=Node(15)
    fizz_buzz = tree.fizz_buzz_tree()
    actual = fizz_buzz.breadth_first()
    expected = ['1', '2', 'Fizz', 'Buzz', '7', 'Fizz',  'FizzBuzz']

    assert actual == expected


def test_k_ary_tree():

    k_tree =k_ary()
    k_tree.root = k_Node(1)
    k_tree.root.childes.append(k_Node(20))
    k_tree.root.childes.append(k_Node(3))
    k_tree.root.childes.append(k_Node(5)) 
    k_tree.root.childes[0].childes.append(k_Node(7)) 
    k_tree.root.childes[0].childes[0].childes.append(k_Node(9)) 
    k_tree.root.childes[0].childes.append(k_Node(2)) 
    k_tree.root.childes[0].childes[1].childes.append(k_Node(4))
    k_tree.root.childes[0].childes[1].childes.append(k_Node(6))
    k_tree.root.childes[0].childes[1].childes.append(k_Node(8)) 
    k_tree.root.childes[1].childes.append(k_Node(11)) 
    k_tree.root.childes[1].childes.append(k_Node(12)) 
    k_tree.root.childes[1].childes.append(k_Node(16)) 
    k_tree.root.childes[2].childes.append(k_Node(15))
    k_tree.root.childes[2].childes.append(k_Node(25))
    k_tree.root.childes[2].childes.append(k_Node(10))

    new_tree = tree_fizz_buzz(k_tree)  
    assert new_tree.root.value == '1'      
    assert new_tree.root.childes[0].value == 'Buzz'
    assert new_tree.root.childes[1].value == 'Fizz'
    assert new_tree.root.childes[2].value == 'Buzz'
    assert new_tree.root.childes[0].childes[0].value == '7' 
    assert new_tree.root.childes[0].childes[0].childes[0].value == 'Fizz'
    assert new_tree.root.childes[0].childes[1].value == '2'
    assert new_tree.root.childes[0].childes[1].childes[0].value == '4'
    assert new_tree.root.childes[0].childes[1].childes[1].value == 'Fizz'
    assert new_tree.root.childes[1].childes[0].value == '11' 
    assert new_tree.root.childes[1].childes[1].value == 'Fizz' 
    assert new_tree.root.childes[1].childes[2].value == '16' 
    assert new_tree.root.childes[0].childes[1].childes[2].value == '8'
    assert k_tree.root.childes[2].childes[0].value == 'FizzBuzz'
    assert k_tree.root.childes[2].childes[1].value == 'Buzz'
    assert k_tree.root.childes[2].childes[2].value == 'Buzz'