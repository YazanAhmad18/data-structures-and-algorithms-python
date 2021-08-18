class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

class Binary_Tree:

    def __init__(self):
        self.root = None

        
    def post_order(self):

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node_value):
                if node_value.left !=None:
                    tree(node_value.left)
                if node_value.right !=None:
                    tree(node_value.right)
                self.values.append(node_value.value)
                return self.values
        
            return tree(self.root)

    def pre_order(self):
     
            self.values=[]
            if self.root == None:
                return "Tree is Empty"

            def tree(node_value):
               self.values.append(node_value.value)
               if  node_value.left !=None:
                    tree(node_value.left)
               if node_value.right!=None:
                    tree(node_value.right)
               return self.values
            return tree(self.root)
        

    def in_order(self):

            self.values=[]
            
            if not self.root:
                return "Tree is Empty"

            def tree(node_value):
                if node_value.left !=None:
                    tree(node_value.left)
                self.values.append(node_value.value)
                if node_value.right !=None:
                    tree(node_value.right)
                return self.values
        
            return tree(self.root)
      

        

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
        
            cur=self.root
            while cur:
                if  value < cur.value : 
                    if cur.left == None: 
                        cur.left = Node(value)
                        break
                    cur = cur.left
                else:
                    if cur.right == None: 
                        cur.right = Node(value)
                        break
                    cur = cur.right

    def Contains(self,value):
        if self.root==None:
            return 'Tree is Empty'

        else:
            cur=self.root
            while cur:
                if cur.value==value:
                    return True
                elif value < cur.value : 
                    if cur.left == None: 
                       return False
                    cur = cur.left
                else:
                    if cur.right == None: 
                        return False
                    cur = cur.right