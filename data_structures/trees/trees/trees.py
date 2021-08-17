class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

class Binary_Tree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        try:

            self.values=[]
         
            if self.root == None:
                return "Tree is Empty"

            def tree(node):
               self.values+=[node.value]
               if node.left:
                    tree(node.left)
               if node.right:
                    tree(node.right)
               return self.values
            
            return tree(self.root)
        except:
            return "Error"

    def in_order(self):
        try:

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node):
                if node.left:
                    tree(node.left)
                self.values+=[node.value]
                if node.right:
                    tree(node.right)
                return self.values
        
            return tree(self.root)
        except:
            return "Error"

        

    def post_order(self):
        try:

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node):
                if node.left:
                    tree(node.left)
                if node.right:
                    tree(node.right)
                self.values+=[node.value]
                return self.values
        
            return tree(self.root)
        except:
            return "Error"

    def max(self):
   
        if not self.root:
                return "Tree is Empty"

        self.max=self.root.value
        def tree(node):
            if node.value>self.max:
                self.max=node.value
            if node.left:
                tree(node.left)
            if node.right:
                tree(node.right)
            return self.max
    
        return tree(self.root)

    def breadth_first(self):
        arr_nodes = [self.root]
        result = []

        if not arr_nodes[0]:
            return 'an Empty Tree'

        while arr_nodes:
            node=arr_nodes[0]
            if node.left:
                arr_nodes.append(node.left)
            if node.right:
                arr_nodes.append(node.right)
            result.append(arr_nodes[0].value)
            arr_nodes = arr_nodes[1:]
            
        return result

    def fizz_buzz_tree(self):
        root = self.root
        new_fizz_buzz_tree = Binary_Tree()

        if not root:
            return "tree is Empty"

        def result_fizz_buzz(node):
            if node%3==0 and node%5==0:
                return ('FizzBuzz')
            elif node % 3==0:
                return ('Fizz')
            elif node % 5 == 0:
                return ('Buzz')
            else:
                return str(node)

        def tree(node):
            tree_node = Node(result_fizz_buzz(node.value))
            if node.left:
                tree_node.left = tree(node.left)
            if node.right:
                tree_node.right = tree(node.right)
            return tree_node
        new_fizz_buzz_tree.root = tree(root)

        return (new_fizz_buzz_tree)
                


class Binary_Search_Tree(Binary_Tree):

    def add(self,value):

        if self.root == None:
            self.root = Node(value)
        else:
        
            current=self.root
            while current:
                if  value < current.value : 
                    if current.left == None: 
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: 
                        current.right = Node(value)
                        break
                    current = current.right

    def Contains(self,value):
        if self.root==None:
            return 'Tree is Empty'

        else:
            current=self.root
            while current:
                if current.value==value:
                    return True
                elif value < current.value : 
                    if current.left == None: 
                       return False
                    current = current.left
                else:
                    if current.right == None: 
                        return False
                    current = current.right


if __name__ == '__main__':
    tree = Binary_Tree()
    tree.root=Node(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(5)
    tree.root.left.right=Node(7)
    tree.root.right.right=Node(9)
    tree.root.left.right.left=Node(15)
    new_tree = ((tree.fizz_buzz_tree()))
    print(new_tree.breadth_first())
    print(tree.breadth_first())