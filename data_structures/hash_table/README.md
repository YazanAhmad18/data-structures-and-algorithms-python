# Hashtables
<!-- Short summary or background information -->
### Hashing is a technique that is used to uniquely identify a specific object from a group of similar objects

# Challenge
<!-- Description of the challenge -->
### Implement a Hashtable Class

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* add:
  * time `O(1)`
  * space `O(1)`
* get:
  * time `O(1)`
  * space `O(1)`
* contains:
  * time `O(1)`
  * space `O(1)`
* hash:
  * time `O(n)`
  * space `O(1)`

## API
<!-- Description of each method publicly available in each of your hashtable -->
* add
  * Arguments: key, value
  * Returns: nothing
  * This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
* get
  * Arguments: key
  * Returns: Value associated with that key in the table
* contains
  * Arguments: key
  * Returns: Boolean, indicating if the key exists in the table already.
* hash
  * Arguments: key
  * Returns: Index in the collection for that key

## Solution
<!-- Show how to run your code, and examples of it in action -->
| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| HashTable                                      | [hash_table.py](hash_table/hash_table.py)|
| Test HashTable                                 | [test_hash_table.py](tests/test_hash_table.py)|

# Challenge Summary - Code Challenge: Class 31
<!-- Description of the challenge -->
### Write a function called repeated word that finds the first word to occur more than once in a string

## Whiteboard Process
<!-- Embedded whiteboard image -->
![hashmap-repeated-word](img/hashmap-repeated-word.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* time `O(n)`
* space `O(1)`

## Solution
<!-- Show how to run your code, and examples of it in action -->
| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| repeated_word                                  | [repeated_word.py](hash_table/repeated_word.py)|
| test_repeated_word                             | [test_repeated_word.py](tests/test_repeated_word.py)|

# Challenge Summary - Code Challenge: Class 32 - Hashmap Tree Intersection
<!-- Description of the challenge -->
### Feature Tasks

### Find all values found to be in 2 binary trees

* Write a function called tree intersection
* Arguments: two binary trees
* Return: array

## Whiteboard Process
<!-- Embedded whiteboard image -->
![hashmap-tree-intersection](img/hashmap-tree-intersection.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* time `O(2n)`
* space `O(n)`

## Solution
<!-- Show how to run your code, and examples of it in action -->
| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| Hashmap Tree Intersection            | [hash_tree_intersection.py](hash_table/hash_tree_intersection.py)|
| test_hashmap_tree_intersection  | [test_hash_tree_intersection.py](tests/test_hash_tree_intersection.py)|


# Challenge Summary - Code Challenge: Class 33 - Hashmap LEFT JOIN
<!-- Short summary or background information -->
### Implement a simplified LEFT JOIN for 2 Hashmaps

## Challenge
<!-- Description of the challenge -->
### Write a function that LEFT JOINs two hashmaps into a single data structure

* Write a function called left join
* Arguments: two hash maps
  * The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
  * The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

* Return: The returned data structure that holds the results is up to you. It doesn't need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* time `O(n^2)`
* space `O(n)`

## Solution
<!-- Embedded whiteboard image -->
![hashmap-left-join](img/hashmap-left-join.jpg)

| Table Of Content               | Links                                                                        |
| ------------------------------ | ---------------------------------------------------------------------------- |
| Hashmap Left Join               | [hashmap_left_join.py](hash_table/hashmap_left_join.py)       |
| Test Hashmap Left Join         | [test_hashmap_left_join.py](tests/test_hashmap_left_join.py) |