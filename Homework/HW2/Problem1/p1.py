# Hash Table
from collections import deque


class HashTable:
    def __init__(self, size):
        self.size = size  # we take in the size that we want our hash table to be - in this case it will always be 100 so we can use some constant "m" to hash
        self.hash_table = self.create_buckets()  # here we create the buckets for our hash table

    def print_table(self):
        print(self.hash_table)

    def create_buckets(self):
        return [deque() for _ in range(self.size)]  # here we create 100 buckets with linked lists in each of them so they can grow dynamically

    def search(self, key):  # adapted from the CLRS pseudocode
        index = 0
        for i in range(len(key)):  # Hashing method taken from 11.3-2
            index += i  # we add up all the values of each of the letters of the key
        index %= self.size  # then we apply the division method onto it
        data = self.hash_table[index]

        for elem in data:   # the "while data not null" we look through each of the keys in each bucket
            data_key = elem[0]   # this id our data object with the key and value elements
            data_val = elem[1]

            if data_key == key:  # if our data object key is what our search key is we found it and return the value
                return data_val

        return "none"   # otherwise, it is not there so we return nul or "none" in this case

    def insert(self, key, value):
        obj = self.search(key)  # searching whether the key exists or not

        index = 0
        for i in range(len(key)):  # Hashing method taken from 11.3-2
            index += i   # we add up all the values of each of the letters of the key
        index %= self.size   # then we apply the division method onto it
        elem = [key, value]  # creating our object for insertion

        data = self.hash_table[index]  # finding the correct bucket to add our new key to
        if obj is "none":  # if object doesn't exist then we just add the element to our bucket
            data.append(elem)
        else:
            for elem in data:  # else find the key in our bucket and update its value
                if elem[0] == key:
                    elem[1] = value


hash_table = HashTable(100) # Setting the size and "m" for our Hash

file = open("input.txt", 'r')
output = open("output.txt", "w+")

for line in file:
    line = line.split()
    if line[0] == "put":
        hash_table.insert(line[1], line[2])  # our insert command
    elif line[0] == "get":
        output.write(hash_table.search(line[1]) + "\n")  # formatting to make it look nice

output.close()