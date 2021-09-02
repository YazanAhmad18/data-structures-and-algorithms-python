class Node:
    def __init__(self,value):
        self.value= value
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, value):
       
        node = Node(value)
        if self.head == None:
            self.head = node
            return self.head.value
        else:
            current = self.head
            self.head = node
            self.head.next = current
            return self.head.value


    def includes(self,value):
        if self.head:
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value")

    def __str__(self):
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str
        else:
             data_str = 'NULL'
             return data_str
  

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)







 
   


