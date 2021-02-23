from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
    # set counter to start at 0
    counter = 0 
    # create an empty for the array
    arr = []

    while counter < size:
      #append the linked list to the array
      thing = LinkedList()
      #appending thing to the list as many times as we need
      arr.append(thing)
      counter += 1
    
    return arr

  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    hash_number = hash(key) % self.size
    return hash_number


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.


  def insert(self, key, value):
    # step1: we need to get the hash num from key
    index = self.hash_func(key)
    # step2: access index of self.array
    
    # step3: call the append func from linked list, assign (value) that was passed into this func
    #if key exists in linked list
    number_of_key = self.arr[index].find(key)
    if number_of_key == -1:
      self.arr[index].append((key, value))
    else:




    #True increment counter 
    # copy out the current counter
    # delete the node 
    # increment the counter
    # append the new values into the linked list
    #False save that one in the linked list since it will not be changed


    # We need to return the data, and ship it to the print_key_values method. 
    

  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    pass



