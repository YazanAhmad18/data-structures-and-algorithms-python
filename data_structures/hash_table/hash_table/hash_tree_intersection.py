from hash_table.hash_table import Hashtable
from hash_table.trees import * 

def tree_intersection(binary_tree1,binary_tree2):
    """
    Write a function called tree intersection
    Arguments: two binary trees
    Return: array
    """
    array=[]
    hashtable=Hashtable()

    if not  binary_tree1.root or not binary_tree2.root:
        return "one of the trees is empty"

    tree_arr1=binary_tree1.pre_order()
    tree_arr2=binary_tree2.pre_order()
    print(tree_arr1)
    print( tree_arr2)

    for test_sample in tree_arr1:
        hashtable.add(test_sample,test_sample)

    for element in tree_arr2:
        if hashtable.contains(element):
            array+=[element]
    
    if array==[]:
        return "input Trees there is not intersection"

    return array

if __name__=='__main__':
# tree 1
    binary_tree1=Binary_Tree()
    binary_tree1.root=Node(150)
    binary_tree1.root.left=Node(100)
    binary_tree1.root.right=Node(250)
    binary_tree1.root.left.left=Node(75)
    binary_tree1.root.left.right=Node(160)
    binary_tree1.root.right.left=Node(200)
    binary_tree1.root.right.right=Node(350)
    binary_tree1.root.left.right.left=Node(125)
    binary_tree1.root.left.right.right=Node(175)
    binary_tree1.root.right.right.left=Node(300)
    binary_tree1.root.right.right.right=Node(500)
# tree 2
    binary_tree2=Binary_Tree()
    binary_tree2.root=Node(42)
    binary_tree2.root.left=Node(100)
    binary_tree2.root.right=Node(600)
    binary_tree2.root.left.left=Node(15)
    binary_tree2.root.left.right=Node(160)
    binary_tree2.root.right.left=Node(200)
    binary_tree2.root.right.right=Node(350)
    binary_tree2.root.left.right.left=Node(125)
    binary_tree2.root.left.right.right=Node(175)
    binary_tree2.root.right.right.left=Node(4)
    binary_tree2.root.right.right.right=Node(500)

    print(tree_intersection(binary_tree1,binary_tree2))
