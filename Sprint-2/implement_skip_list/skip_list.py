import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * (level + 1)


class SkipList:
    MAX_LEVEL = 16

    def __init__(self):
        self.level = 0
        self.head = Node(None, self.MAX_LEVEL)

    def random_level(self):
        level = 0

        while level < self.MAX_LEVEL and random.random() < 0.5:
            level += 1

        return level

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # Find where the new value belongs.
        for level in range(self.level, -1, -1):
            while (
                current.next[level] is not None
                and current.next[level].value < value
            ):
                current = current.next[level]

            update[level] = current

        current = current.next[0]

        # If the value already exists, do not insert it again.
        if current is not None and current.value == value:
            return

        new_level = self.random_level()

        # Increase the list's height if needed.
        if new_level > self.level:
            for level in range(self.level + 1, new_level + 1):
                update[level] = self.head

            self.level = new_level

        new_node = Node(value, new_level)

        # Connect the new node at each of its levels.
        for level in range(new_level + 1):
            new_node.next[level] = update[level].next[level]
            update[level].next[level] = new_node

    def __contains__(self, value):
        current = self.head

        # Start at the highest level and move down.
        for level in range(self.level, -1, -1):
            while (
                current.next[level] is not None
                and current.next[level].value < value
            ):
                current = current.next[level]

        current = current.next[0]

        return current is not None and current.value == value

    def to_list(self):
        values = []
        current = self.head.next[0]

        # The bottom level contains every value in sorted order.
        while current is not None:
            values.append(current.value)
            current = current.next[0]

        return values
