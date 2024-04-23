ctrl + k + v
# NODES
A node contains data and links to other nodes.
 - data could be an integer, a string, decimal, an array, or null 
 - links are reffered to as pointers
    - if link is null, it denotes that you've reached the end of the node path
![node_image](../study_materials/images/node.webp)
If we want to delete node_b we simply just change the link on node_a to point directly to node_c
![node_link](../study_materials/images/node_link.gif)
```python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# creating nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# linking nodes
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# getting data from nodes
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
```

# LINKED LIST
When inserting elements into an **array**, the other elements keep being copied and moved around the memory to make space for the new elements which is time and memory consuming. Lists in python are dynamic and they prealocate space even if it's not used later.

Insert/delete element at the bebrginning - O(1)
Insert/delete element at the end - O(n)
Linked list traversal - O(n)
Accessing element by value - O(n)

A linked list is comprised of a series of nodes.
 - Head node is at the beginning
 - Tail node has the link set to null
![linked_list](../study_materials/images/linked_list.svg)

Linked list operations
 - adding nodes
 - removing nodes
 ![linked_list_remove](../study_materials/images/linked_list_remove.webp)
 - finding a node
 - traversing the linked list
```python
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
```
# DOUBLY LINKED LIST
# QUEUE
# STACK
# HASH MAP
# RECURSION
# ASYMPTOTIC NOTATION
# PATTERN SEARCHING
# SORTING ALGORITHMS
# TREES
## TREE TRAVERSAL
# DIVIDE AND CONQUER
# HEAPS AND HEAPSORT
# GRAPHS AND GRAPH SEARCH
# GREEDY ALGORITHMS
# PATHFINDING ALGORITHMS