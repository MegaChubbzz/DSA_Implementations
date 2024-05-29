'''Implenting hash table'''


class HashTable:
    def hashKey(self, key):
        return abs(hash(key))

    def insert(self, key, value):
        pass

    def remove(self, key):
        pass

    def search(self, key):
        pass


class ChainingHashTableItem:
    def __init__(self, itemKey, itemValue):
        self.key = itemKey
        self.value = itemValue
        self.next = None


class ChainingHashTable(HashTable):
    def __init__(self, initialCapacity=11):
        self.table = [None] * initialCapacity

    def insert(self, key, value):
        bucket_index = self.hashKey(key) % len(self.table)
        item = self.table[bucket_index]
        previous = None
        while item != None:
            if key == item.key:
                item.value = value
                return True
            previous = item
            item = item.next
        if self.table[bucket_index] == None:
            self.table[bucket_index] = ChainingHashTableItem(key, value)
        else:
            previous.next = ChainingHashTableItem(key, item)
        return True

    def remove(self, key):
        bucket_index = self.hashKey(key) % len(self.table)
        item = self.table[bucket_index]
        previous = None
        while item != None:
            if key == item.key:
                if previous == None:
                    self.table[bucket_index] = item.next
                else:
                    previous.next = item.next
                return True
            previous = item
            item = item.next
        return False

    def search(self, key):
        bucket_index = self.hashKey(key) % len(self.table)
        item = self.table[bucket_index]
        while item != None:
            if key == item.key:
                return item.value
            item = item.next
        return None


class OpenAddressingBucket:
    def __init__(self, bucket_key=None, bucket_value=None):
        self.key = bucket_key
        self.value = bucket_value

    def isEmpty(self):
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()


class OpenAddressingHashTable(HashTable):
    def __init__(self, initialCapacity):
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * initialCapacity

    def probe(self, key, i):
        pass

    def insert(self, key, value):
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                break
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    self.table[bucket_index].value = value
                    return True
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            if self.table[bucket_index].isEmpty():
                self.table[bucket_index] = OpenAddressingBucket(key, value)
                return True
        return False

    def remove(self, key):
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return False
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    self.table[bucket_index] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL
                    return True
        return False

    def search(self, key):
        for i in range(len(self.table)):
            bucket_index = self.probe(key, i)
            if self.table[bucket_index] is OpenAddressingBucket.EMPTY_SINCE_START:
                return None
            if self.table[bucket_index] is not OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                if key == self.table[bucket_index].key:
                    return self.table[bucket_index].value
        return None


class LinearProbingHashTable(OpenAddressingHashTable):
    def __init__(self, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)

    def probe(self, key, i):
        return (self.hashKey(key) + i) % len(self.table)


class QuadraticProbingHashTable(OpenAddressingHashTable):
    def __init__(self, c1=1, c2=1, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)
        self.c1 = c1
        self.c2 = c2

    def probe(self, key, i):
        return (self.hashKey(key) + self.c1 * i + self.c2 * i * i) % len(self.table)


class DoubleHashingHashTable(OpenAddressingHashTable):
    def __init__(self, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)

    def h2(self, key):
        return 7 - self.hashKey(key) % 7

    def probe(self, key, i):
        return (self.hashKey(key) + i * self.h2(key)) % len(self.table)
    
