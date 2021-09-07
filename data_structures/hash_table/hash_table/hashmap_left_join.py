from hash_table.hash_table import Hashtable



def left_join(hashtable1, hashtable2):
    """
    Write a function that LEFT JOINs two hashmaps into a single data structure.
    Arguments: two hash maps
        - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
        - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Return:
    """
    arr_key = []
    for sample_nodes in hashtable1._buckets:
        if sample_nodes != None:
            node = sample_nodes.head
            current_value = node.value
            while current_value:
                key = list(current_value.keys())[0]
                if hashtable2.contains(key):
                    arr_key += [[key, current_value[key], hashtable2.get(key)]]
                else:
                    arr_key += [[key, current_value[key], None]]
                if node.next:
                    node = node.next
                    current_value = node.value
                else:
                    break

    if not arr_key:
        return "right table is empty"

    return arr_key




if __name__ == "__main__":
    hash_table1 = Hashtable()
    hash_table1.add('fond', 'enamored')
    hash_table1.add('wrath', 'anger')
    hash_table1.add('diligent', 'employed')
    hash_table1.add('outift', 'garb')
    hash_table1.add('guide', 'usher')

    hash_table2 = Hashtable()
    hash_table2.add('fond', 'averse')
    hash_table2.add('wrath', 'delight')
    hash_table2.add('diligent', 'idle')
    hash_table2.add('guide', 'follow')
    hash_table2.add('flow', 'jam')

    print(left_join(hash_table1, hash_table2))

