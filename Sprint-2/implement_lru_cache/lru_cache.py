
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.previous = self.head

    def add_to_front(self, node):
        node.next = self.head.next
        node.previous = self.head

        self.head.next.previous = node
        self.head.next = node

    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous

    def remove_last(self):
        node = self.tail.previous
        self.remove(node)
        return node


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit = limit
        self.cache = {}
        self.order = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        self.order.remove(node)
        self.order.add_to_front(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.order.remove(node)
            self.order.add_to_front(node)
            return

        if len(self.cache) >= self.limit:
            oldest_node = self.order.remove_last()
            del self.cache[oldest_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.order.add_to_front(new_node)
