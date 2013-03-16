"""
Question

    Implement a hash table with collision resolution by chaining.

Solution

    This hash table uses the division method for creating hash functions: a key
    is mapped into one of the slots by taking the remainder of the key divided
    by the number of slots.
"""
import unittest


class HashTable(object):

    def __init__(self, initial_size):
        self.size = initial_size
        self.table = [[]] * initial_size

    def hash_function(self, value):
        return hash(value) % self.size

    def insert(self, key, value):

        slot = self.table[self.hash_function(key)]
        if not slot:
            self.table[self.hash_function(key)] = [(key, value)]
        else:
            slot.append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        # Python equivalent for iterate list and remove element
        self.table[index] = [(k, v) for (k, v) in self.table[index]
                             if not k == key]

    def get(self, key):
        slot = self.table[self.hash_function(key)]
        for (k, v) in slot:
            if k == key:
                return v


class HashTableTest(unittest.TestCase):

    def test_insert(self):
        hash_table = HashTable(3)
        hash_table.insert("Berlin", 3531201)
        hash_table.insert("New York City", 8244910)
        hash_table.insert("San Francisco", 812826)
        hash_table.insert("London", 8174100)

    def test_get(self):
        hash_table = HashTable(3)
        self.assertEqual(hash_table.get("Berlin"), None)
        hash_table.insert("Berlin", 3531201)
        hash_table.insert("New York City", 8244910)
        hash_table.insert("San Francisco", 812826)
        hash_table.insert("London", 8174100)
        self.assertEqual(hash_table.get("Berlin"), 3531201)

    def test_delete(self):
        hash_table = HashTable(3)
        hash_table.insert("Berlin", 3531201)
        hash_table.insert("New York City", 8244910)
        hash_table.insert("San Francisco", 812826)
        hash_table.insert("London", 8174100)
        hash_table.delete("London")
        self.assertEqual(hash_table.get("London"), None)


if __name__ == '__main__':
    unittest.main()
