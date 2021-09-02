from hash_table.linked_list import Linkedlist



class Hashtable:
    def __init__(self,size=1024):
        self.size=size
        self._buckets=[None]*self.size
        self.str_bucket=''






    def add(self,key,value):

        """
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        Arguments:
            key: a string
            value: any type
        Returns: nothing
        """

        index=self.hash(key)

        if self._buckets[index]==None:
           self._buckets[index]=Linkedlist()
       
        self._buckets[index].append({key:value})


    def get(self,key):
        """
        This function will search in the hashtable about the key and return the value
        Arguments:
            key: string
        Returns: Value associated with that key in the table
        """
        index=self.hash(key)
        if self._buckets[index]==None:
            return "Key does not exsist the hash table"
        else:
            if self._buckets[index].head ==None:
                return "Bucket is empty"
            else:
                current=self._buckets[index].head
                while current:
                    if list(current.value.keys())[0]==key:
                        return current.value[key]
                    current=current.next
                return "Key dose not exsist the hash table!"



    
    def contains(self,key):

        """
        This function will check if the there is a value for the key
        Arguments:
            key: string
        Returns: Boolean, indicating if the key exists in the table already.
        """
        idx_hash=self.hash(key)
        if self._buckets[idx_hash]==None:
            return False
        else:
                current=self._buckets[idx_hash].head
                if current==None:
                    return False
                else:
                    while current:
                        if list(current.value.keys())[0]==key:
                            return True
                        current=current.next
                    return False

    def hash(self,key):

        """
         this function will determine the index in hash
         Arguments: 
            Key: string or int
        Returns: Index in the collection for that key
        """
        if type(key)==int:
            ASSCI_Sumation=key
        else:
            ASSCI_Sumation=sum([ord(char) for char in key])
       
        index= (ASSCI_Sumation*11) % self.size
        return index

    def __str__(self):

        for bucket in self._buckets:
            if bucket != None :
                self.str_bucket += bucket.__str__()

        return self.str_bucket


if __name__ == "__main__":
    hashtable = Hashtable()
    hashtable.add('name', 'yazan')
    hashtable.add('name', 'ahmad')
    print(f"Get name: {hashtable.get('name')}")
    print(f"Hash name: {hashtable.contains('name')}")
    print(f"Index in hash for name: {hashtable.hash('name')}")
    print(f"Get phone: {hashtable.get('phone')}")
    print(f"Hash phone: {hashtable.contains('phone')}")
    print(f"Index in hash for phone: {hashtable.hash('phone')}")
    print(hashtable.__str__())

    





 


        