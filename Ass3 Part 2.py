class ChainedHashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with a default size of 10 buckets.
        Each bucket is an empty list to store key-value pairs.
        """
        self.size = size  # Total number of buckets
        self.table = [[] for _ in range(size)]  # Create empty lists for chaining
        self.element_count = 0  # Keep track of the number of elements

    def hash_function(self, key):
        """
        Simple hash function: use built-in hash function and take modulo of size.
        This ensures the index is within the bounds of the table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert the key-value pair into the hash table. If the key already exists,
        update the value.
        """
        index = self.hash_function(key)  # Compute the index for the key
        # Check if the key already exists in the chain
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  # If key found, update its value
                self.table[index][i] = (key, value)
                return
        # Otherwise, append the key-value pair to the list
        self.table[index].append((key, value))
        self.element_count += 1  # Increment element count
        # Resize if load factor exceeds 0.75
        if self.load_factor() > 0.75:
            self.resize()

    def search(self, key):
        """
        Search for a key in the hash table and return its associated value.
        Return None if the key is not found.
        """
        index = self.hash_function(key)  # Compute index for the key
        for k, v in self.table[index]:  # Traverse the chain at the index
            if k == key:  # If key is found
                return v  # Return the associated value
        return None  # If key not found, return None

    def delete(self, key):
        """
        Delete a key-value pair from the hash table. Return True if the deletion
        was successful, or False if the key was not found.
        """
        index = self.hash_function(key)  # Compute index for the key
        for i, (k, v) in enumerate(self.table[index]):  # Traverse the chain at the index
            if k == key:  # If key is found
                del self.table[index][i]  # Delete the key-value pair
                self.element_count -= 1  # Decrement the element count
                return True  # Return success
        return False  # Return False if key was not found

    def load_factor(self):
        """
        Calculate the load factor of the hash table, defined as the ratio of
        the number of elements to the number of buckets.
        """
        return self.element_count / self.size

    def resize(self):
        """
        Resize the hash table by doubling its size and rehashing all elements.
        This is necessary to maintain efficiency as the load factor increases.
        """
        new_size = self.size * 2  # Double the size
        new_table = [[] for _ in range(new_size)]  # Create new empty buckets

        # Rehash all key-value pairs into the new table
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_size  # Compute new index
                new_table[new_index].append((key, value))  # Move key-value pair to new bucket

        self.size = new_size  # Update the size
        self.table = new_table  # Replace the old table with the new one

    def display(self):
        """
        Display the contents of the hash table by showing the key-value pairs
        stored in each bucket.
        """
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage of hash table with chaining
hash_table = ChainedHashTable()
hash_table.insert("apple", 100)
hash_table.insert("banana", 150)
hash_table.insert("grape", 200)
hash_table.display()

print("Search for 'apple':", hash_table.search("apple"))
hash_table.delete("banana")
hash_table.display()
