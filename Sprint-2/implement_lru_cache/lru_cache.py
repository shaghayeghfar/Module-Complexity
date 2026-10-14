class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit = limit
        self.cache = {}

        # Most recently used node is near the head.
        # Least recently used node is near the tail.
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.previous = self.head

    def remove_node(self, node):
        # Connect the node's neighbours to each other.
        node.previous.next = node.next
        node.next.previous = node.previous

    def add_to_front(self, node):
        # Insert the node immediately after the head.
        node.next = self.head.next
        node.previous = self.head

        self.head.next.previous = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        # Using a value makes it the most recently used.
        self.remove_node(node)
        self.add_to_front(node)

        return node.value

    def set(self, key, value):
        # If the key already exists, update its value.
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove_node(node)
            self.add_to_front(node)
            return

        # If the cache is full, remove the least recently used node.
        if len(self.cache) >= self.limit:
            oldest_node = self.tail.previous

            self.remove_node(oldest_node)
            del self.cache[oldest_node.key]

        # Create the new node and add it to the front.
        new_node = Node(key, value)

        self.cache[key] = new_node
        self.add_to_front(new_node)
