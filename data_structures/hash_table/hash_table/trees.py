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
      

        
