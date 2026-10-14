from typing import Optional


class Node:
    __slots__ = ("value", "next", "previous")

    def __init__(self, value: str) -> None:
        self.value: str = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def push_head(self, value: str) -> Node:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        return new_node

    def pop_tail(self) -> str:
        if self.tail is None:
            raise IndexError("Cannot pop from an empty list")

        removed_node = self.tail
        self.remove(removed_node)

        return removed_node.value

    def remove(self, node: Node) -> None:
        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        node.next = None
        node.previous = None
