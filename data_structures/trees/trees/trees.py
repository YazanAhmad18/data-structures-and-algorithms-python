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