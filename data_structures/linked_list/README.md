# Singly Linked List
<!-- Short summary or background information -->
* A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail). Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.
## Challenge
<!-- Description of the challenge -->
* Create a Node class that has properties for the value stored in the Node, and traversed on it and doing some function
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* learn a lot about LinkedList how to deal with it and traversed throw it
## API
<!-- Description of each method publicly available to your Linked List -->
### The class should contain the following methods
#### insert
* Arguments: value
* Returns: nothing
* Adds a new node with that value to the head of the list with an O(1) Time performance.
#### includes
*Arguments: value
*Returns: Boolean
*Indicates whether that value exists as a Node's value somewhere within the list.
### to string
* Arguments: none
* Returns: a string representing all the values in the Linked List, formatted as:
* "{ a } -> { b } -> { c } -> NULL"


| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| linked_list                                    | [linked_list.py](linked_list/linked_list.py)|
| test_linked_list                               | [test_linked_list.py](tests/test_linked_list.py)|