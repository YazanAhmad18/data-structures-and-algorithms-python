from hash_table.hash_table import Hashtable



def left_join(hashtable1, hashtable2):
    """
    Write a function that LEFT JOINs two hashmaps into a single data structure.
    Arguments: two hash maps
        - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
        - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
    """

    final_result = []

    list_buckets = hashtable1.hashtable_dictonary()

    for key, value in list_buckets.items():
     

        if hashtable2.contains(key):
            final_result += [[key, value, hashtable2.get(key)]]

        else:
            final_result += [[key, value, None]]

    if not final_result:
        return "Right HashTable Empty"

    return final_result




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

