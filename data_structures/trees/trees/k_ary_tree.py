class k_Node:
    def __init__(self, value):
        self.value = value
        self.childes = []

class k_ary:
    def __init__(self):
        self.root = None

def tree_fizz_buzz(tree):
    if tree.root == None:
        return "This is empty tree no node in this tree"

    new_k_tree = tree
    nodetree = new_k_tree.root
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return 'FizzBuzz'
        elif value % 3 == 0:
            return 'Fizz'
        elif value % 5 == 0:
            return 'Buzz'
        else:
            return str(value)

    def traversal(node_k):
        node_k.value = fizz_buzz(node_k.value)
        if len(node_k.childes) > 0:
            for child in node_k.childes :
                traversal(child)
    traversal(nodetree)
    return new_k_tree


